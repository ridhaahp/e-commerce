import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'payment_type': ['Credit Card', 'Debit Card', 'Credit Card', 'Cash', 'Debit Card', 'Credit Card', 'Cash', 'Debit Card']
})

# Create a Streamlit app
st.title("Professional Payment Method Dashboard")

# Sidebar with filter options
st.sidebar.header("Filter Options")
selected_payment_type = st.sidebar.selectbox("Select Payment Method", df['payment_type'].unique())

# Filter the DataFrame based on the selected payment type
filtered_df = df[df['payment_type'] == selected_payment_type]

# Visualize the data using Altair
st.subheader(f"Chart of {selected_payment_type} Payments")

# Altair plot
chart = alt.Chart(filtered_df).mark_bar().encode(
    alt.X("payment_type:N", title="Payment Method"),
    alt.Y("count():Q", title="Count"),
    tooltip=[alt.Tooltip("count()", title="Count")]
).properties(width=600, height=400)

st.altair_chart(chart, use_container_width=True)

# Display additional information
st.write("Additional Information:")
st.write(f"Total {selected_payment_type} payments: {len(filtered_df)}")

# Show the original data table
st.subheader("Original Data Table")
st.write(filtered_df)
