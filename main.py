# Entry point to orchestrate ETL process
│   │   
│   │   from extract import extract_data
│   │   from transform import transform_data
│   │   from load import load_data
│   │   
│   │   def run_etl():
│   │       """Run the full ETL pipeline."""
│   │       raw_data = extract_data(source="api")
│   │       transformed_data = transform_data(raw_data)
│   │       load_data(transformed_data)
│   │       print("ETL process completed successfully.")
│   │   
│   │   if __name__ == "__main__":
│   │       run_etl()
│   
