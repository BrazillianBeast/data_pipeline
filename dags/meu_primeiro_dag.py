from airflow.import DAG
from air

with DAG(
    'meu_primeiro_dag',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag: