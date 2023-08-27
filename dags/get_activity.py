"""
get_activity
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from airflow.models import Variable
from astro import sql as aql
import pandas as pd
import pendulum

from airflow.models import Variable
import requests

@aql.dataframe(task_id="fetch_activity")
def fetch_activity_func():
    r = requests.get(Variable.get('API'))
    return r.json()

@aql.dataframe(task_id="print_activity")
def print_activity_func(fetch_activity: pd.DataFrame):
    print(fetch_activity)

default_args={
    "owner": "Krutika R,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2023-08-27", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Krutika R": "mailto:krutikar2514@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cllm2u1ui002z01g1juotedwm/cloud-ide/clltirbx0000901j6e3xcri0y/clltirl1x004t01mirhh3iotm",
    },
)
def get_activity():
    fetch_activity = fetch_activity_func()

    print_activity = print_activity_func(
        fetch_activity,
    )

dag_obj = get_activity()
