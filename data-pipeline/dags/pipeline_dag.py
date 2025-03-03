from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'pipeline_de_dados',
    default_args=default_args,
    schedule_interval='@once'
)

# Tarefa 1: Ingestão de dados brutos
ingestao = BashOperator(
    task_id='ingestao_raw',
    bash_command='echo "Copiando dados para data/raw/..." && cp /app/data_original.csv /app/data/raw',
    dag=dag
)

# Tarefa 2: Processamento com PySpark para dados Trusted
processamento = BashOperator(
    task_id = "processamento_trusted",
    bash_command = 'echo "Processando dados com PySpark..." && spark-submit /app/scripts/process_raw_to_trusted.py',
    dag=dag
)

# Tarefa 3: Processamento com PySpark para camada Analytic
analise = BashOperator(
    task_id = "analise_analytic",
    bash_command = 'echo "Gerando camada Analytic..." && spark-submit /app/scripts/process_trusted_to_analytic.py',
    dag=dag 
)

ingestao >> processamento >> analise