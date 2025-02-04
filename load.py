# Load data into the database or data warehouse
│   │   
│   │   import sqlite3
│   │   import pandas as pd
│   │   from config import DATA_SOURCE
│   │   
│   │   def load_data(df, table_name="e_commerce_data"):
│   │       """Load data into a SQLite database."""
│   │       conn = sqlite3.connect(DATA_SOURCE)
│   │       df.to_sql(table_name, conn, if_exists="replace", index=False)
│   │       conn.close()
│   │       print(f"Data successfully loaded into table {table_name}")
│   │   
│   │   if __name__ == "__main__":
│   │       sample_data = {"product_name": ["Item A", "Item B"], "price": [100, 200]}
│   │       df = pd.DataFrame(sample_data)
│   │       load_data(df)
