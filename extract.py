# Extract data from APIs, databases, or files
│   │   
│   │   import requests
│   │   import pandas as pd
│   │   import json
│   │   from config import API_URL, HEADERS, DATA_SOURCE
│   │   import sqlite3
│   │   
│   │   def extract_from_api():
│   │       """Extract data from an API and return as a DataFrame."""
│   │       response = requests.get(API_URL, headers=HEADERS)
│   │       if response.status_code == 200:
│   │           data = response.json()
│   │           df = pd.DataFrame(data)
│   │           return df
│   │       else:
│   │           raise Exception(f"Failed to fetch data: {response.status_code}")
│   │   
│   │   def extract_from_database():
│   │       """Extract data from a SQLite database and return as a DataFrame."""
│   │       conn = sqlite3.connect(DATA_SOURCE)
│   │       query = "SELECT * FROM e_commerce_data"
│   │       df = pd.read_sql_query(query, conn)
│   │       conn.close()
│   │       return df
│   │   
│   │   def extract_data(source="api"):
│   │       """Extract data from the specified source."""
│   │       if source == "api":
│   │           return extract_from_api()
│   │       elif source == "database":
│   │           return extract_from_database()
│   │       else:
│   │           raise ValueError("Unsupported data source")
│   │   
│   │   if __name__ == "__main__":
│   │       df = extract_data(source="api")
│   │       print(df.head())
