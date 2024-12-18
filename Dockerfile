FROM apache/airflow:2.5.1

# Install additional dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy DAGs and plugins
COPY dags /opt/airflow/dags
COPY plugins /opt/airflow/plugins

# Set the working directory
WORKDIR /opt/airflow
