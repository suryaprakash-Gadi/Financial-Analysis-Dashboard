class Visualization:
    @staticmethod
    def print_analysis(company_id, sales_growth, profit_growth, roe):
        print(f"\nAnalysis for {company_id}:")
        print("Sales Growth:")
        for period, value in sales_growth.items():
            print(f"  {period}: {value:.2f}%")
        print("Profit Growth:")
        for period, value in profit_growth.items():
            print(f"  {period}: {value:.2f}%")
        print("Return on Equity:")
        for period, value in roe.items():
            print(f"  {period}: {value:.2f}%")