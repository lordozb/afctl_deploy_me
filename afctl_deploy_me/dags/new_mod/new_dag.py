
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner': 'afctl_deploy_me',
'start_date': datetime.now()
}

dag = DAG(dag_id='new', default_args=default_args, schedule_interval='@once')

task_1 = DummyOperator(task_id='task_1', dag=dag)
task_2 = DummyOperator(task_id='task_2', dag=dag)

task_1 >> task_2

