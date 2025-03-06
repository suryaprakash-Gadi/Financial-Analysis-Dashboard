

import os

class Config:
    API_BASE_URL = "https://stockticker.tech/server/api/company.php"
    API_KEY = os.getenv("API_KEY")  # Fetch API key from environment variables

    DB_CONFIG = {
        'host': os.getenv("DB_HOST", "localhost"),
        'user': os.getenv("DB_USER", "root"),
        'password': os.getenv("DB_PASSWORD", ""),
        'database': os.getenv("DB_NAME", "financial_analysis")
    }

    COMPANIES_FILE = "data/companies.xlsx"
