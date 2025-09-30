# TenderNed Data Fetcher

This Python script fetches procurement publication data from the [TenderNed API](https://www.tenderned.nl/) and saves the results into a CSV file for further analysis.

## Features

* **API integration**: Connects to the TenderNed public API (`/publicaties` endpoint).
* **Pagination support**: Automatically retrieves all available pages of results.
* **Data flattening**: Handles nested JSON structures by flattening them into a flat dictionary for CSV export.
* **Flexible parameters**: Supports filtering results by publication/closing date presets and CPV codes.
* **CSV export**: Outputs a clean, tabular dataset (`tenderned_results.csv`) with consistent column headers.

## How it works

1. Sends HTTP GET requests to the TenderNed API using the specified query parameters.
2. Iterates through all available pages until no more results are found.
3. Flattens nested JSON responses into a dictionary format.
4. Collects all unique keys to ensure consistent CSV headers.
5. Saves the complete dataset into `tenderned_results.csv`.

## Requirements

* Python 3.7+
* Dependencies:

  ```bash
  pip install requests
  ```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/tenderned-data-fetcher.git
   cd tenderned-data-fetcher
   ```
2. Run the script:

   ```bash
   python run7day.py
   ```
3. The results will be saved to:

   ```
   tenderned_results.csv
   ```

## Configuration

You can adjust the query parameters in the script:

* **`page`**: Starting page (default: `0`).
* **`size`**: Number of results per page (default: `100`).
* **`publicatieDatumPreset` / `sluitingsDatumPreset`**: Filter by publication/closing date presets.
* **`cpvCodes`**: Provide one or multiple CPV codes to filter results.

Example:

```python
params = {
    "page": 0,
    "size": 100,
    "publicatieDatumPreset": "AF7",
    "sluitingsDatumPreset": "TKM",
    "cpvCodes": ["48000000-8", "72000000-5"],
    "useExperimentalFeature": "false"
}
```

## Output

* A CSV file named **`tenderned_results.csv`** containing all the retrieved and flattened results.
* Each row represents a publication, and each column corresponds to a flattened JSON key.
