import pandas as pd

class DataProcessor:
    def process_financial_data(self, raw_data):
        if not raw_data or not isinstance(raw_data, dict):
            print("Invalid raw data:", raw_data)
            return None
        
        print("Processing raw data:", raw_data)  # Debug
        
        pl_data = raw_data.get('data', {}).get('profitandloss', [])
        bs_data = raw_data.get('data', {}).get('balancesheet', [])
        
        if not pl_data or not bs_data:
            print("No profit/loss or balance sheet data found")
            return None
        
        pl_df = pd.DataFrame(pl_data)
        bs_df = pd.DataFrame(bs_data)
        
        df = pd.DataFrame({
            'year': pl_df['year'],
            'sales': pl_df['sales'].astype(float),
            'profit': pl_df['net_profit'].astype(float),
            'net_income': pl_df['net_profit'].astype(float),
            'equity': (bs_df['equity_capital'].astype(float) + bs_df['reserves'].astype(float))
        })
        
        def parse_year(x):
            if pd.isna(x) or not isinstance(x, str):
                return 0  # Invalid years
            if x == 'TTM':
                return 9999  # TTM goes last
            try:
                # Extract the last part and attempt to convert to int
                year_part = x.split()[-1]
                return int(year_part)
            except (ValueError, IndexError):
                # Handle cases like '9m' or malformed strings
                return 0  # Default for non-year formats
        
        df['year_order'] = df['year'].apply(parse_year)
        df = df.sort_values('year_order').drop('year_order', axis=1)
        
        df.fillna(0, inplace=True)
        print("Processed DataFrame:\n", df)  # Debug
        return df