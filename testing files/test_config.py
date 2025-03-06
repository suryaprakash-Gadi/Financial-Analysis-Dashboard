from sqlalchemy import create_engine
from config.config import Config
import os
from urllib.parse import quote

# Print the configuration for debugging
print("Config settings:")
print(f"API_BASE_URL: {Config.API_BASE_URL}")
print(f"API_KEY: {Config.API_KEY}")
print(f"DB_CONFIG: {Config.DB_CONFIG}")
print(f"COMPANIES_FILE: {Config.COMPANIES_FILE}")

# URL-encode the password to handle special characters
encoded_password = quote(Config.DB_CONFIG['password'])

# Construct and print the connection string
conn_string = (
    f"mysql+pymysql://{Config.DB_CONFIG['user']}:{encoded_password}@"
    f"{Config.DB_CONFIG['host']}/{Config.DB_CONFIG['database']}"
)
print(f"\nConnection string: {conn_string}")

# Test database connection
try:
    engine = create_engine(conn_string)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print(f"Database connection failed: {e}")

# Test companies.xlsx file existence
file_path = Config.COMPANIES_FILE
if os.path.exists(file_path):
    print(f"Found {file_path} successfully!")
else:
    print(f"Error: {file_path} not found!")
