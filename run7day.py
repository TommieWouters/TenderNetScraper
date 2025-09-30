import requests
import csv

# Function to flatten nested dictionaries
def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


# Base URL
base_url = "https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties"

# Parameters (now aligned with the new example URL)
params = {
    "page": 0,
    "size": 100,
    "publicatieDatumPreset": "AF7",
    "sluitingsDatumPreset": "TKM",
    "cpvCodes": ["48000000-8", "72000000-5"],  # multiple values supported
    "useExperimentalFeature": "false"
}

all_results = []

# Fetch all pages
while True:
    print(f"Fetching page {params['page']}...")
    response = requests.get(base_url, params=params)
    print("Request URL:", response.url)  # show the URL being used
    response.raise_for_status()  # ensure errors are caught
    data = response.json()
    
    results = data.get('content', [])
    if not results:
        break
    
    # Flatten each JSON object
    flattened = [flatten_dict(item) for item in results]
    all_results.extend(flattened)
    
    total_pages = data.get('totalPages', 1)
    if params['page'] >= total_pages - 1:  # stop at last page
        break
    
    params['page'] += 1

print(f"Total results fetched: {len(all_results)}")

# Get all CSV column headers
all_keys = sorted(set().union(*[d.keys() for d in all_results]))

# Ensure every row has all keys
for row in all_results:
    for key in all_keys:
        row.setdefault(key, "")

# Write to CSV
with open("tenderned_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_keys)
    writer.writeheader()
    writer.writerows(all_results)

print("Saved to tenderned_results.csv")
