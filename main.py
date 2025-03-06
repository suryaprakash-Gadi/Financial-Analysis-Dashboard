import pandas as pd
import json
import os
from config.config import Config
from src.data_fetcher import DataFetcher
from src.data_processor import DataProcessor
from src.ml_analyzer import MLAnalyzer
from src.database_handler import DatabaseHandler
from src.visualization import Visualization

def main():
    fetcher = DataFetcher()
    processor = DataProcessor()
    analyzer = MLAnalyzer()
    db_handler = DatabaseHandler()
    viz = Visualization()
    
    try:
        companies = pd.read_excel(Config.COMPANIES_FILE, header=1)
        print("Column names:", companies.columns.tolist())
    except Exception as e:
        print(f"Error loading companies.xlsx: {e}")
        return
    
    analysis_results = {}
    
    for company_id in companies['id']:
        print(f"\nProcessing {company_id}...")
        
        raw_data = fetcher.fetch_company_data(company_id)
        if not raw_data:
            print(f"No data returned for {company_id}")
            continue

        processed_data = processor.process_financial_data(raw_data)
        if processed_data is None:
            continue

        sales_growth, profit_growth, roe = analyzer.analyze_financials(processed_data)
        if sales_growth is None:
            continue

        db_handler.save_analysis(company_id, sales_growth, profit_growth, roe)
        viz.print_analysis(company_id, sales_growth, profit_growth, roe)
        
        analysis_results[company_id] = {
            'sales_growth': sales_growth,
            'profit_growth': profit_growth,
            'roe': roe
        }
    
    os.makedirs('data', exist_ok=True)
    with open('data/processed_analysis.json', 'w') as f:
        json.dump(analysis_results, f, indent=4)

if __name__ == '__main__':
    main()