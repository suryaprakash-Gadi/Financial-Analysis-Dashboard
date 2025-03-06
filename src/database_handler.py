from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import Config

# from config.config import Config
import json
from urllib.parse import quote

class DatabaseHandler:
    def __init__(self):
        encoded_password = quote(Config.DB_CONFIG['password'])
        conn_string = (
            f"mysql+pymysql://{Config.DB_CONFIG['user']}:{encoded_password}@"
            f"{Config.DB_CONFIG['host']}/{Config.DB_CONFIG['database']}"
        )
        self.engine = create_engine(conn_string)
        self.Session = sessionmaker(bind=self.engine)

    def save_analysis(self, company_id, sales_growth, profit_growth, roe):
        session = self.Session()
        try:
            query = text(
                "INSERT INTO ml (company_id, sales_growth, profit_growth, roe) "
                "VALUES (:company_id, :sales_growth, :profit_growth, :roe) "
                "ON DUPLICATE KEY UPDATE "
                "sales_growth = VALUES(sales_growth), "
                "profit_growth = VALUES(profit_growth), "
                "roe = VALUES(roe)"
            )
            session.execute(
                query,
                {
                    'company_id': company_id,
                    'sales_growth': json.dumps(sales_growth),
                    'profit_growth': json.dumps(profit_growth),
                    'roe': json.dumps(roe)
                }
            )
            session.commit()
            print(f"Saved analysis for {company_id} to database")
        except Exception as e:
            session.rollback()
            print(f"Database Error: {e}")
        finally:
            session.close()