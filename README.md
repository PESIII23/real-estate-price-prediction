# Real Estate Price Prediction

A modular Python pipeline for predicting house prices using exploratory data analysis, data wrangling, and regression modeling.

---

## Project Structure

```
src/
├── preprocessing/
│   ├── data_prep.py             # Cleaning, wrangling, train/test split
│   └── feature_engineering.py   # Variable selection, X/y split, scaling
├── models/
│   └── model.py                 # Model definitions, training, evaluation
├── notebooks/
│   └── price_prediction_model.ipynb  # EDA and modeling notebook
├── data/
│   ├── raw/                     # Source Excel data
│   └── processed/               # Cleaned data outputs
└── viz/
    └── plotting.py              # Reusable visualization utilities
```

---

## Quick Start

**1. Clone the repository:**
```bash
git clone https://github.com/PESIII23/real-estate-price-prediction.git
cd real-estate-price-prediction
```

**2. Create a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the notebook:**
```
Place the source Excel file in src/data/raw/, then open src/notebooks/price_prediction_model.ipynb.
```

---

## Pipeline Stages

| Stage | Description |
|-------|-------------|
| **1. Data Loading** | Read raw Excel data into a DataFrame |
| **2. EDA** | Statistical summaries, distributions, correlation analysis |
| **3. Data Wrangling** | Handle missing values, remove duplicates, remove outliers |
| **4. Feature Engineering** | Variable selection, X/y separation, scaling/normalization |
| **5. Modeling** | Train and evaluate Linear Regression, Random Forest, Lasso, Ridge |
| **6. Evaluation** | Compare models across multiple train/test splits (80/20, 50/50, 95/5) |

---

## Key Features

- **Exploratory Data Analysis** – Statistical profiling, distribution plots, correlation heatmaps
- **Data Wrangling** – NaN removal, outlier detection, duplicate handling
- **Multiple Models** – Linear Regression, Random Forest, Lasso, Ridge via scikit-learn
- **Back-Testing** – Model comparison across varying train/test split ratios
- **Scaling & Normalization** – StandardScaler and MinMaxScaler support
- **Modular Architecture** – Clean separation across preprocessing, models, and visualization

---

## Tools & Libraries

- Python 3.13+
- pandas, numpy – Data manipulation
- scikit-learn – Modeling, train/test split, scaling
- matplotlib, seaborn – Visualization
- openpyxl – Excel file reading

---

## Support

- Email: pesmithiii7@gmail.com
- Documentation: [Milestone 1]() | [Milestone 2]() | [Milestone 3]()
- Repository: [GitHub](https://github.com/PESIII23/real-estate-price-prediction)
