import pandas as pd
from sklearn.linear_model import LinearRegression

class MLAnalyzer:
    def __init__(self):
        self.model = LinearRegression()

    def analyze_financials(self, processed_data):
        if processed_data is None or processed_data.empty:
            print("No processed data available")
            return None, None, None
        
        print("Analyzing data:\n", processed_data)  # Debug
        
        sales_growth = self._compute_growth_rates(processed_data['sales'])
        profit_growth = self._compute_growth_rates(processed_data['profit'])
        roe = self._compute_roe(processed_data)

        return sales_growth, profit_growth, roe

    def _compute_growth_rates(self, series):
        if series.empty or len(series) < 2:
            return {'10_years': 0, '5_years': 0, '3_years': 0, '1_year': 0}
        
        periods = len(series) - 1
        growth_rates = {
            '10_years': self._compute_cagr(series, min(10, periods)) if periods >= 10 else 0,
            '5_years': self._compute_cagr(series, min(5, periods)) if periods >= 5 else 0,
            '3_years': self._compute_cagr(series, min(3, periods)) if periods >= 3 else 0,
            '1_year': self._compute_cagr(series[:2], 1) if periods >= 1 else 0  # Mar 2023 to Mar 2024
        }
        return growth_rates

    def _compute_cagr(self, series, periods):
        if len(series) <= periods or series.iloc[0] == 0 or series.iloc[-1] == 0:
            return 0
        end_value = series.iloc[-1]
        start_value = series.iloc[0]
        return ((end_value / start_value) ** (1/periods) - 1) * 100

    def _compute_roe(self, df):
        if 'net_income' not in df or 'equity' not in df or df['equity'].eq(0).any():
            return {'10_years': 0}
        roe_series = df['net_income'] / df['equity'] * 100
        return {'10_years': roe_series.mean() if not roe_series.empty else 0}