import streamlit as st
import pandas as pd

# Add a slider to the sidebar:
data_set_number = st.select_slider(
    "Dataset n (# of users)",
    options=[
        "2002",
        "2006",
        "4002",
        "4006",
        "6002",
        "6006",
        "8002",
        "8006",
        "10002",
        "10006",
    ],
)

# Display data_set_number value on main screen
st.write(f"When dataset *n* (# of users)= {data_set_number}")

# Read chosen dataset column
streamlit_data = pd.read_csv("./streamlit_data.csv", index_col=0)
data = streamlit_data[f"{data_set_number}"]

table_index = [
    "1st recommendation",
    "2nd",
    "3rd",
    "4th",
    "5th",
]
table_columns = [
    "2002",
    "2006",
    "4002",
    "4006",
    "6002",
    "6006",
    "8002",
    "8006",
    "10002",
    "10006",
]
page_mapping = [
    "Housings",
    "GIRO",
    "Transactions",
    "Contributions",
    "Contact",
    "Retirements",
    "Education",
    "Appointments",
    "e-Medical",
]

billy_recommendations = {}
for i, col in enumerate(table_columns[: table_columns.index(data_set_number) + 1]):
    page_numbers = streamlit_data[f"{col}"].iloc[0].split(",")
    page_names = [page_mapping[int(page_num)] for page_num in page_numbers]
    billy_recommendations[col] = page_names

evelyn_recommendations = {}
for i, col in enumerate(table_columns[: table_columns.index(data_set_number) + 1]):
    page_numbers = streamlit_data[f"{col}"].iloc[1].split(",")
    page_names = [page_mapping[int(page_num)] for page_num in page_numbers]
    evelyn_recommendations[col] = page_names

st.write("Billy Martin's recommendations")
st.dataframe(pd.DataFrame(data=billy_recommendations, index=table_index))

st.write("Evelyn Kane's recommendation")
st.dataframe(pd.DataFrame(data=evelyn_recommendations, index=table_index))
