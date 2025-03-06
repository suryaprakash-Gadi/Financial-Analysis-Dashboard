from src.data_fetcher import DataFetcher
from src.data_processor import DataProcessor
from src.ml_analyzer import MLAnalyzer
from src.visualization import Visualization

# Fetch, process, and analyze data
fetcher = DataFetcher()
processor = DataProcessor()
analyzer = MLAnalyzer()
visualizer = Visualization()

company_id = "JIOFIN"
raw_data = fetcher.fetch_company_data(company_id)
processed_data = processor.process_financial_data(raw_data)
sales_growth, profit_growth, roe = analyzer.analyze_financials(processed_data)

# Visualize results
if sales_growth and profit_growth and roe:
    visualizer.print_analysis(company_id, sales_growth, profit_growth, roe)
    print(f"Visualization completed for {company_id}")
else:
    print(f"Failed to process or analyze data for {company_id}")