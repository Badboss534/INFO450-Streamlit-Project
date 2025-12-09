import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np # For creating dummy data

st.title("FEMA Disaster Relief Dashboard")

#--- Load FEMA dataset--
# Option 2: Or use a raw GitHub or LinkedIn file link
# df = pd.read_csv("https://raw.githubusercontent.com/username/repo/main/IndividualAssistanceHousingRegistrantsLargeDisasters.csv")

# Temporary dummy data for demonstration. Please replace this with your actual data loading.
if 'df' not in locals():
    data = {
        'repairAmount': np.random.randint(500, 10000, 100),
        'tsaEligible': np.random.choice([0, 1], 100)
    }
    df = pd.DataFrame(data)
    st.info("Using dummy data. Please uncomment and update the `pd.read_csv` line with your actual data source.")

st.subheader("Data Preview")
st.write(df.head())

#--- Histogram of Repair Amount--
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(df, x="repairAmount", nbins=30,
title="Distribution of Repair Amounts")
st.plotly_chart(fig_hist)

#--- Boxplot of Repair Amount by TSA Eligibility--
st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(df, x="tsaEligible", y="repairAmount",
title="Repair Amount by TSA Eligibility",
labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)",
"repairAmount": "Repair Amount"})
st.plotly_chart(fig_box)

#--- Optional text summary--
st.markdown("*Insight:* Compare the central tendency and spread of repair amounts for TSA-eligible vs. non-eligible households.*")
