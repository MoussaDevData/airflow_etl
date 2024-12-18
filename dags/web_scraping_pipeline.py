from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'web_scraping_pipeline',
    default_args=default_args,
    description='A web scraping pipeline',
    schedule_interval=timedelta(days=1),
)

def fetch_web_data():
    response = requests.get('https://group.bnpparibas')
    with open('/opt/airflow/data/web_data/response.html', 'w') as f:
        f.write(response.text)

fetch_web_data_task = PythonOperator(
    task_id='fetch_web_data',
    python_callable=fetch_web_data,
    dag=dag,
)

fetch_web_data_task
