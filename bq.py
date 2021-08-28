import pandas as pd

import os


def bq_func1():
    credential_file = "/Users/husnusensoy/Documents/code/learn-python-in-a-day/analytics-bootcamp-323516-04308ccfbcba.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_file

    project_id = "analytics-bootcamp-323516"
    sql = """
    select * from `analytics-bootcamp-323516.week1.trips_2015`  limit 3
    """
    df = pd.read_gbq(sql, project_id=project_id, dialect="standard", use_bqstorage_api=True)

    print(df)


if __name__ == '__main__':
    bq_func1()
