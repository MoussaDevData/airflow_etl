from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

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
    'etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    df = pd.read_csv('/opt/airflow/data/input_data/data.csv')
    return df

def transform_data(**kwargs):
    ti = kwargs['ti']
    df = ti.xcom_pull(task_ids='extract_data')
    json_data = df.to_json(orient='records')
    return json_data

def load_data(**kwargs):
    ti = kwargs['ti']
    json_data = ti.xcom_pull(task_ids='transform_data')
    with open('/opt/airflow/data/output_data/data.json', 'w') as f:
        f.write(json_data)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    provide_context=True,
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    provide_context=True,
    python_callable=load_data,
    dag=dag,
)

extract_task >> transform_task >> load_task
