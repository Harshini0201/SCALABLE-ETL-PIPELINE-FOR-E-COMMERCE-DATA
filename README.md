# Scalable ETL Pipeline for E-Commerce Data
│   │   
│   │   This project is a **Scalable ETL Pipeline** designed to extract, transform, and load e-commerce data.
│   │   
│   │   ## Features
│   │   - **Extract** data from APIs and databases.
│   │   - **Transform** data by cleaning and normalizing it.
│   │   - **Load** the processed data into a SQLite database.
│   │   - **Dockerized** for easy deployment.
│   │   - **Supports workflow automation** via Apache Airflow.
│   │   
│   │   ## Installation
│   │   1. Clone the repository:
│   │      ```bash
│   │      git clone https://github.com/your-repo/scalable-etl-pipeline.git
│   │      cd scalable-etl-pipeline
│   │      ```
│   │   2. Install dependencies:
│   │      ```bash
│   │      pip install -r requirements.txt
│   │      ```
│   │   
│   │   ## Usage
│   │   Run the ETL pipeline:
│   │   ```bash
│   │   python main.py
│   │   ```
│   │   
│   │   ## Docker Usage
│   │   Build and run using Docker:
│   │   ```bash
│   │   docker build -t etl-pipeline .
│   │   docker run etl-pipeline
│   │   ```
│   │   
│   │   ## Folder Structure
│   │   - `extract.py`: Extracts data from APIs or databases.
│   │   - `transform.py`: Cleans and normalizes the data.
│   │   - `load.py`: Loads data into a database.
│   │   - `config.py`: Stores configuration settings.
│   │   - `main.py`: Orchestrates the ETL process.
│   │   - `Dockerfile`: Contains Docker setup instructions.
│   │   - `requirements.txt`: Lists required dependencies.
