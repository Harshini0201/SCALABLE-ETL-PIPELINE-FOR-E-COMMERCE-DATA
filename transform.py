# Clean, normalize, and process the data
│   │   
│   │   import pandas as pd
│   │   
│   │   def clean_data(df):
│   │       """Remove duplicates and handle missing values."""
│   │       df = df.drop_duplicates()
│   │       df = df.fillna(method='ffill')
│   │       return df
│   │   
│   │   def normalize_data(df):
│   │       """Normalize column names and format data types."""
│   │       df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
│   │       return df
│   │   
│   │   def transform_data(df):
│   │       """Apply data transformation steps."""
│   │       df = clean_data(df)
│   │       df = normalize_data(df)
│   │       return df
│   │   
│   │   if __name__ == "__main__":
│   │       sample_data = {"Product Name": ["Item A", "Item B", "Item A"], "Price": [100, 200, None]}
│   │       df = pd.DataFrame(sample_data)
│   │       transformed_df = transform_data(df)
│   │       print(transformed_df.head())
