# Streamlit Dashboard: Solar Country Comparison

## Overview

An interactive dashboard to compare solar potential across Benin, Sierra Leone, and Togo.

## Features

- Select countries and metrics.
- Interactive boxplots and bar charts.
- Summary statistics (mean, median, std).

## How to Run Locally

1. Install requirements:
   pip install streamlit pandas seaborn matplotlib

markdown
Copy
Edit 2. Run the app:
streamlit run app/main.py

markdown
Copy
Edit

## Deployment

Deploy via [Streamlit Community Cloud](https://streamlit.io/cloud).

## Folder Structure

app/
├── main.py
├── utils.py
scripts/
└── README.md

markdown
Copy
Edit

## Development Notes

- CSV files are read from `data/` (not pushed to Git).
- Commit message for initial version: `feat: basic Streamlit UI`
