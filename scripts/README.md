# 🌞 Cross-Country Solar Energy Insights

This project is a **Streamlit dashboard** that helps visualize solar energy data (like Global Horizontal Irradiance - GHI) across different countries and regions. It shows helpful charts and tables, and lets you interact with the data using dropdowns and sliders.

---

## 📂 Project Structure

```
solar-challenge-week1/
├── app/
│   ├── main.py        # Main Streamlit app file
│   ├── utils.py       # Helper functions for loading and processing data
├── scripts/
│   ├── README.md      # (Optional) Notes for scripts if needed
├── data/              # (Local CSV files here, not uploaded to GitHub)
```

---

## 🚀 How to Run Locally

1. **Clone the project**

```bash
git clone https://github.com/emexnord/solar-challenge-week1
cd solar-challenge-week1
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app/main.py
```

This will open the dashboard in your browser at [http://localhost:8501](http://localhost:8501).

---

## ⚙️ Features

- Dropdown to select country.
- Boxplot and other charts to explore solar data.
- Table showing top regions based on GHI or other metrics.
- Interactive design using Streamlit widgets.

---

## 🧹 Notes

- The `data/` folder is ignored in `.gitignore` and only used locally.
- Data files must be available locally to run the app.
- Make sure column names in your CSV match what the app expects.

---

## 📌 Development Progress

- ✅ Basic UI with dropdown and boxplot
- ✅ Data loading utility functions

---
