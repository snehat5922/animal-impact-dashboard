# 🐾 Animal Impact & Food Sustainability Analytics Dashboard

A Streamlit-based interactive analytics dashboard that explores the ethical and sustainability impacts of food production by analyzing the number of animal lives lost per kilogram of food produced.

The project helps users understand the relative impact of different food categories and promotes data-driven awareness regarding sustainable food choices.

---

# 📌 Project Overview

Food production affects millions of animals globally. Different food categories require varying levels of animal harvesting, resulting in significant differences in animal lives lost per kilogram of food produced.

This dashboard provides:

* Food impact rankings
* Sustainability analysis
* Interactive visualizations
* Comparative food assessments
* Data-driven recommendations
* Ethical consumption insights

---

# 🎯 Objectives

* Analyze direct animal lives lost per kilogram of food production.
* Compare food categories based on animal welfare impact.
* Identify sustainable food choices.
* Visualize food impact through interactive charts.
* Provide actionable sustainability recommendations.

---

# 📊 Dataset Information

Dataset Name:

Animal Lives Lost Direct Dataset

Features:

| Column              | Description                             |
| ------------------- | --------------------------------------- |
| Entity              | Food Category                           |
| Code                | Country Code                            |
| Year                | Observation Year                        |
| lives_per_kg_direct | Animal lives lost per kilogram produced |

Examples of food categories:

* Beef
* Chicken
* Pork
* Fish
* Shrimp
* Eggs
* Crab
* Lamb
* Turkey
* Milk

---

# 🚀 Dashboard Features

## 📈 Executive Summary

* Total Food Categories
* Highest Impact Food
* Lowest Impact Food
* Average Animal Impact
* KPI Cards
* Interactive Rankings

---

## 🐔 Food Impact Analysis

Interactive Visualizations:

* Treemap Analysis
* Pie Charts
* Distribution Charts
* Food Impact Breakdown

---

## 🏆 Sustainability Rankings

Provides:

* Food Ranking Table
* Sustainable Food Ordering
* Lowest Impact Foods
* Highest Impact Foods

---

## 📊 Comparative Insights

Compare two foods side-by-side:

* Animal lives lost comparison
* Impact difference calculation
* Sustainability assessment

---

## 💡 Recommendations Dashboard

Provides:

* Best food choices
* High impact food warnings
* Sustainability recommendations
* Ethical consumption insights

---

# 🛠 Technology Stack

## Frontend

* Streamlit

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly

## Deployment

* Streamlit Community Cloud

---

# 📂 Project Structure

animal-impact-dashboard/

├── app.py

├── data/
│   └── animal-lives-lost-direct.csv

├── pages/
│   ├── 1_Executive_Summary.py
│   ├── 2_Food_Impact_Analysis.py
│   ├── 3_Sustainability_Rankings.py
│   ├── 4_Comparative_Insights.py
│   └── 5_Recommendations.py

├── assets/
│   ├── logo.png
│   └── banner.png

├── utils/
│   ├── data_loader.py
│   └── insights.py

├── requirements.txt

├── README.md

└── .streamlit/
└── config.toml

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/animal-impact-dashboard.git
cd animal-impact-dashboard
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📈 Dashboard Pages

## 1️⃣ Executive Summary

Overview of:

* Food Categories
* Average Impact
* Highest Impact Foods
* Lowest Impact Foods

---

## 2️⃣ Food Impact Analysis

Visualize:

* Food category impacts
* Treemap distribution
* Impact shares

---

## 3️⃣ Sustainability Rankings

Identify:

* Most sustainable foods
* Least sustainable foods
* Ranking comparisons

---

## 4️⃣ Comparative Insights

Compare:

* Two food categories
* Impact differences
* Sustainability metrics

---

## 5️⃣ Recommendations

Receive:

* Sustainable alternatives
* Ethical consumption guidance
* Data-driven recommendations

---

# 🤖 Key Insights

The dashboard automatically generates insights such as:

* Highest animal impact food category
* Lowest animal impact food category
* Average animal impact score
* Sustainability recommendations
* Ethical food consumption observations

---

# 🌍 Real-World Applications

This project can be used for:

* Sustainability Research
* Environmental Awareness Programs
* Animal Welfare Studies
* Educational Demonstrations
* Data Visualization Portfolios
* Academic Mini Projects

---

# 🚀 Deployment

Deploy the dashboard using Streamlit Cloud:

1. Create GitHub Repository
2. Upload Project Files
3. Connect Repository to Streamlit Cloud
4. Select app.py
5. Deploy

---

# 📸 Future Enhancements

Potential improvements:

* Carbon Footprint Analysis
* Water Usage Analytics
* Greenhouse Gas Emissions Comparison
* Global Food Sustainability Dashboard
* Machine Learning Recommendations
* Multi-Dataset Integration

---

# 👨‍💻 Author

Animal Impact & Food Sustainability Analytics Dashboard

Developed using:

* Python
* Streamlit
* Pandas
* Plotly

---

# 📜 License

This project is developed for educational, research, and sustainability awareness purposes.

Feel free to use, modify, and extend the project for learning and research.
