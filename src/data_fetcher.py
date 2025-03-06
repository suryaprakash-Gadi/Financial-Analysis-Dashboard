import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import Config

class DataFetcher:
    def __init__(self):
        self.base_url = Config.API_BASE_URL
        self.api_key = Config.API_KEY

    def fetch_company_data(self, company_id):
        url = f"{self.base_url}?id={company_id}&api_key={self.api_key}"
        try:
            response = requests.get(url, timeout=5)  # Added timeout
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            print(f"API Timeout for {company_id}")
            return None
        except requests.RequestException as e:
            print(f"API Error for {company_id}: {e}")
            return None
