import streamlit as st
import pandas as pd
import os
import seaborn as sns

def run_bq_sql(sql, project_id="analytics-bootcamp-323516"):
    credential_file = "/Users/husnusensoy/Documents/code/learn-python-in-a-day/analytics-bootcamp-323516-04308ccfbcba.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_file

    df = pd.read_gbq(sql, project_id=project_id, dialect="standard", use_bqstorage_api=True)

    return df


st.title("An analysis on Taxi Trips of Newyork")
st.markdown("""We will do some staff with streamlit
* Seaborn chart
* Google BQ connectivity
  * Data sampling (TABLESAMPLE)
* **Pandas** Dataframes
""")

st.header("Chapter 1: Bring some data from BQ")


@st.cache
def calculate_total_count():
    count = run_bq_sql("select count(1) n from `analytics-bootcamp-323516.week1.trips_2015`")

    return count.n[0]


n = calculate_total_count()
st.text(f"Total number of rows in the dataset to be analyzed {n}")


@st.cache
def topK(n=3):
    return run_bq_sql(f"select * from `analytics-bootcamp-323516.week1.trips_2015`  limit {n}")


st.dataframe(topK())

st.text("I did some BQ things...")

st.header("Chapter 2: Sampling & Charts")


@st.cache
def afew_pickup_locations():
    return run_bq_sql("""
    SELECT
  vendor_id,
  pickup_longitude lon,
  pickup_latitude lat
FROM
  `analytics-bootcamp-323516.week1.trips_2015` TABLESAMPLE SYSTEM(1 PERCENT)
LIMIT
  1000
    """)


df = afew_pickup_locations()

# st.dataframe(df)

st.map(df)


@st.cache
def fare_amount():
    return run_bq_sql("""
    SELECT
  fare_amount,
  log(case when fare_amount < 0 then 0 else fare_amount end + 1) as fare_amount_log1p
FROM
  `analytics-bootcamp-323516.week1.trips_2015` TABLESAMPLE SYSTEM(1 PERCENT)
LIMIT
  1000
    """)


df = fare_amount()

fig1 = sns.displot(data=df, x="fare_amount", kde=True)
fig2 = sns.displot(data=df, x="fare_amount_log1p", kde=True)

st.pyplot(fig1)
st.pyplot(fig2)

selected_value = st.sidebar.selectbox("Column Name",["fare_amount","passenger_count"])

st.text(f"{selected_value} is picked.")