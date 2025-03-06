from src.data_fetcher import DataFetcher

# Initialize the fetcher
fetcher = DataFetcher()

# Test fetching data for a sample company (e.g., JIOFIN)
company_id = "JIOFIN"
data = fetcher.fetch_company_data(company_id)

# Print the result
if data:
    print(f"Data for {company_id}:")
    print(data)
else:
    print(f"Failed to fetch data for {company_id}")