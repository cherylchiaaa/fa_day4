import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real Estate Analytics Dashboard", layout="wide")
st.title("🏠 Real Estate Analytics Dashboard")

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=20, freq="D")

property_type = np.random.choice(
    ["Condo", "Landed", "Apartment"], size=20
)

location = np.random.choice(
    ["Kuala Lumpur", "Selangor", "Penang"], size=20
)

price = np.random.randint(300000, 1500000, size=20)
size_sqft = np.random.randint(600, 3500, size=20)
bedrooms = np.random.randint(1, 6, size=20)

df = pd.DataFrame({
    "Listing Date": dates,
    "Property Type": property_type,
    "Location": location,
    "Price (RM)": price,
    "Size (sqft)": size_sqft,
    "Bedrooms": bedrooms
})

st.dataframe(df)

st.subheader("Line Chart: Price Trends Over Time")
line_df = df.set_index("Listing Date")["Price (RM)"]
st.line_chart(line_df)