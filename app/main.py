import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_country_data, get_summary_stats


st.set_page_config(layout="wide", page_title="Solar Comparison Dashboard")

st.title("🔆 Cross-Country Solar Energy Insights")

# --- File loading ---
filepaths = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierraleone_clean.csv",
    "Togo": "data/togo_clean.csv",
}

df_all = load_country_data(filepaths)
metrics = ["GHI", "DNI", "DHI"]

# --- Sidebar filters ---
st.sidebar.title("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries", options=list(filepaths.keys()), default=list(filepaths.keys())
)
selected_metric = st.sidebar.selectbox("Select Metric", options=metrics)

# --- Filter data ---
filtered_df = df_all[df_all["Country"].isin(selected_countries)]

# --- KPI Summary ---
st.subheader("📊 Summary Statistics")
summary_df = get_summary_stats(filtered_df, metrics)
st.dataframe(summary_df)

# --- Boxplot ---
st.subheader(f"📦 Boxplot for {selected_metric}")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y=selected_metric, ax=ax)
st.pyplot(fig)

# --- Ranking Bar Chart ---
st.subheader("🏆 Country Ranking by Average GHI")
rank_df = df_all.groupby("Country")["GHI"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
rank_df.plot(kind="bar", color="orange", ax=ax2)
ax2.set_ylabel("Average GHI")
st.pyplot(fig2)
