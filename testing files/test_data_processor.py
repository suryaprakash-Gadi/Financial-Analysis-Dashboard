from src.data_fetcher import DataFetcher
from src.data_processor import DataProcessor

# Fetch data
fetcher = DataFetcher()
company_id = "JIOFIN"
raw_data = fetcher.fetch_company_data(company_id)

# Process data
processor = DataProcessor()
processed_data = processor.process_financial_data(raw_data)

# Print result
if processed_data is not None:
    print(f"Processed data for {company_id}:\n", processed_data)
else:
    print(f"Failed to process data for {company_id}")