import streamlit as st
import pandas as pd
from PIL import Image

# Generate mock data
barbra_martin_recommendations = {
    25: ["transactions", "appointments", "giro"],
    31: ["demo", "contributions", "contact"],
    49: ["education", "contact", "contributions"],
    56: ["retirements", "e-medical", "appointments"],
}

barbra_martin_features = {
    25: ["S$3673", "0"],
    31: ["S$4872", "0"],
    49: ["S$5533", "2"],
    56: ["S$1000", "2"],
}

# Streamlit's slider
barbra_age = st.select_slider("Barbra Martin's age", options=[25, 31, 49, 56, "all"])

# Barbra Martin's features by age
st.write("Barbra Martin")

col1, col2, col3 = st.beta_columns(3)  # Layout features in 3 columns
col1.write(f"👱🏻‍♀️: **{barbra_age} years old**")
col2.write(f"💵: **{barbra_martin_features[barbra_age][0]}**")
col3.write(f"👨‍👩‍👧‍👧: **{barbra_martin_features[barbra_age][1]}**")

# Barbra Martin's recommendations by age
st.write("")
st.write("")
st.write("Page recommendations for Barbra Martin")

rec1, rec2, rec3 = barbra_martin_recommendations[barbra_age]

col1, col2, col3 = st.beta_columns(3)  # Layout recommendations in 3 columns
col1.write("1st Recommendation : ")
col1.image(Image.open(f"img/{rec1}.png"), use_column_width=True)
col2.write("2nd : ")
col2.image(Image.open(f"img/{rec2}.png"), use_column_width=True)
col3.write("3rd : ")
col3.image(Image.open(f"img/{rec3}.png"), use_column_width=True)
