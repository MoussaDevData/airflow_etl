# ETL Pipeline with Apache Airflow using Docker

This project demonstrates a simple ETL pipeline using Apache Airflow, Docker, and Docker Compose. It includes:

- **ETL Pipeline**: Reads a CSV file, transforms it into JSON, and saves the JSON file.
- **Web Scraping Pipeline**: Fetches data from a website and saves it as an HTML file.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

```plaintext
bnpp_airflow/
│
├── dags/
│   ├── etl_pipeline.py
│   └── web_scraping_pipeline.py
│
├── data/
│   ├── input_data/
│   │   └── data.csv
│   ├── output_data/
│   │   └── data.json
│   └── web_data/
│       └── response.html
│
├── logs/
│   └── ...
│
├── config/
│   └── airflow.cfg
│
├── Dockerfile
│   
├── docker-compose.yml
│ 
├── requirements.txt
│
├── README.md
│
└── setup.py
```
## Getting Started

### Step 1: Clone the Repository

```bash
git clone [https://github.com/your-username/etl_project.git](https://github.com/MoussaDevData/airflow_etl.git)
cd etl_project
```
### Step 2: Set Up Environment Variables

Create a `.env` file in the root directory of the project with the following content:

```env
AIRFLOW_UID=1000  # Use a default value, you can change it if necessary
AIRFLOW_PROJ_DIR=./  # Project directory
```
### Step 3: Build and Run the Docker Containers

#### Build the Docker images:

```bash
docker-compose build
```

### Initialize the Airflow Database

#### Run the following command:

```bash
docker-compose up airflow-init
```

### Start the Airflow Services

#### Run the following command:

```bash
docker-compose up
```

### Access the Airflow Web Interface

Open your browser and go to [http://localhost:8080](http://localhost:8080).

---

### Step 4: Configure and Run the DAGs

1. **Access the Airflow Web Interface**:
   - Log in with the default credentials:
     - **Username**: `airflow`
     - **Password**: `airflow`

2. **Enable the DAGs**:
   - Navigate to the "DAGs" tab.
   - Find the `etl_pipeline` and `web_scraping_pipeline`.
   - Enable them by toggling the switch next to each DAG.

3. **Run the DAGs**:
   - Click on the DAG name to access its details page.
   - Click the "Trigger DAG" button to manually run the DAG.

---

### DAGs Overview

#### ETL Pipeline (`etl_pipeline.py`)

- Reads a CSV file.
- Transforms it into JSON.
- Saves the JSON file.

#### Web Scraping Pipeline (`web_scraping_pipeline.py`)

- Fetches data from a website.
- Saves it as an HTML file.

---

### Custom Operators

Define custom operators in the `plugins` directory. For example, create a custom operator in `custom_operators.py`.

---

### Data

#### Input Data

The input CSV file (`data.csv`) is located in the `data/input_data/` directory.

#### Output Data

The transformed JSON file (`data.json`) is saved in the `data/output_data/` directory.

#### Web Data

The fetched HTML file (`response.html`) is saved in the `data/web_data/` directory.

---

### Logs

Logs are stored in the `logs/` directory.

---

### Configuration

The Airflow configuration file (`airflow.cfg`) is located in the `config/` directory.

---


### Dockerfile

The `Dockerfile` is used to build the Docker image for the Airflow environment.

### Docker Compose

The `docker-compose.yml` file defines the services and volumes for the Airflow environment.

---

### Requirements

The `requirements.txt` file lists the Python dependencies required for the project.

---

### Setup

The `setup.py` file is used to install the project as a Python package.
