import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA Disaster Relief Dashboard")

# Link to professor's Google Cloud bucket file
df = pd.read_csv("fema_sample.csv")

# Load FEMA dataset
@st.cache_data
def load_data():
    df = pd.read_csv(url)

    # Basic cleaning to match the notebook
    important_cols = [
        "tsaEligible",
        "repairAmount",
        "residenceType",
        "damagedStateAbbreviation",
        "grossIncome"
    ]
    df = df.dropna(subset=important_cols)

    return df

df = load_data()

# Data preview
st.subheader("Data Preview")
st.write(df.head())

# Histogram of repairAmount
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(
    df,
    x="repairAmount",
    nbins=40,
    title="Distribution of Repair Amounts"
)
fig_hist.update_layout(
    xaxis_title="Repair Amount",
    yaxis_title="Count"
)
st.plotly_chart(fig_hist)

st.markdown(
    "Most households have lower repair amounts, and a smaller number of cases "
    "have very high repair costs."
)

# Boxplot of repairAmount by tsaEligible
st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(
    df,
    x="tsaEligible",
    y="repairAmount",
    title="Repair Amount by TSA Eligibility",
    labels={
        "tsaEligible": "TSA Eligible (1 = Yes, 0 = No)",
        "repairAmount": "Repair Amount"
    }
)
st.plotly_chart(fig_box)

st.markdown(
    "TSA eligible households tend to have higher repair amounts and a wider spread "
    "compared to non eligible households."
)

