from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['test@yourdomain.com'],
    'email_on_failure': False,
    'email_on_retry': False
}

DAG_ID = "new_dag"

dag = DAG(
    dag_id=DAG_ID,
    default_args=default_args,
    description='Scheduled Apache Airflow DAG',
    schedule_interval='* 1 * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
)

say_hello = BashOperator(
        task_id='say_hello',
        bash_command="echo hello",
        dag=dag
    )

say_goodbye = BashOperator(
        task_id='say_goodbye',
        bash_command="echo goodbye",
        dag=dag
    )

say_hello >> say_goodbye