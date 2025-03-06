from src.data_fetcher import DataFetcher
from src.data_processor import DataProcessor
from src.ml_analyzer import MLAnalyzer

# Fetch and process data
fetcher = DataFetcher()
processor = DataProcessor()
company_id = "JIOFIN"
raw_data = fetcher.fetch_company_data(company_id)
processed_data = processor.process_financial_data(raw_data)

# Analyze data
analyzer = MLAnalyzer()
sales_growth, profit_growth, roe = analyzer.analyze_financials(processed_data)

# Print results
if sales_growth and profit_growth and roe:
    print(f"Analysis for {company_id}:")
    print("Sales Growth:", sales_growth)
    print("Profit Growth:", profit_growth)
    print("ROE:", roe)
else:
    print(f"Failed to analyze data for {company_id}")