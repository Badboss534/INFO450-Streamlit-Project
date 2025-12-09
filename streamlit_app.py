import streamlit as st
import pandas as pd
import plotly.express as px

st.write("Authors: Tasrique Chowdhury")

st.title("FEMA Disaster Relief Dashboard")

df = pd.read_csv("fema_sample.csv")

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(df, x="repairAmount", nbins=30,
title="Distribution of Repair Amounts")
st.plotly_chart(fig_hist)

st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(df, x="tsaEligible", y="repairAmount",
title="Repair Amount by TSA Eligibility",
labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)",
"repairAmount": "Repair Amount"})
st.plotly_chart(fig_box)

st.markdown("*Insight:* Compare the central tendency and spread of repair amounts for TSA-eligible vs. non-eligible households.*")




