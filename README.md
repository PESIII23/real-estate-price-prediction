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
| **2. Data Cleaning** | Standardize column names, handle missing values, and apply initial cleaning |
| **3. Data Transformation** | Normalize units, apply log transforms, detect and handle outliers |
| **4. Exploratory Data Analysis (EDA)** | Generate statistical summaries, distribution plots, and correlation analysis |
| **5. Feature Engineering** | Feature selection (SFS and others), X/y split, scaling, and baseline error check |
| **6. Export Modeling Data** | Save the engineered DataFrame for modeling |
| **7. Modeling** | Train and evaluate models (Linear Regression, Random Forest, Lasso, Ridge) |
| **8. Evaluation & Back-Testing** | Compare models across multiple train/test splits (80/20, 50/50, 95/5), plot residuals, and check for overfitting |
| **9. Iteration & Interpretation** | Analyze errors, refine features, experiment with advanced models, and summarize results |

---

## Key Features

- **End-to-End Modular Pipeline** – Clean separation of data cleaning, transformation, EDA, feature engineering, modeling, and evaluation for reproducibility and maintainability
- **Robust Data Cleaning & Transformation** – Automated column standardization, missing value handling, normalization, log transforms, and outlier detection
- **Comprehensive EDA** – Statistical summaries, distribution plots, and correlation heatmaps for deep data understanding
- **Advanced Feature Selection** – Multiple techniques benchmarked (SelectKBest, RFE, Random Forest, SFS), with SFS integrated for optimal performance
- **Flexible Modeling** – Supports Linear Regression, Random Forest, Lasso, and Ridge, with easy extension to other models
- **Cross-Validation & Back-Testing** – Consistent use of k-fold CV and multiple train/test splits (80/20, 50/50, 95/5) for robust model comparison
- **Automated Export** – Engineered features and modeling data are saved for downstream use and reproducibility
- **Clear Visualizations** – Publication-ready plots for distributions, relationships, and feature importance
- **Scalable & Extensible** – Designed for easy adaptation to new datasets, features, or modeling approaches

---

## Tools & Libraries

- Python 3.13+
- pandas, numpy – Data manipulation
- scikit-learn – Modeling, train/test split, scaling
- matplotlib, seaborn – Visualization
- openpyxl – Excel file reading

---

## Feature Selection Learnings & Tradeoffs

Throughout the development of this project, several feature selection techniques were evaluated to optimize model performance and interpretability:

- **Univariate Selection (SelectKBest with f_regression):**
  - Simple and fast, but only captures linear relationships between each feature and the target.
  - Resulted in higher RMSE and lower R² compared to more advanced methods.

- **Recursive Feature Elimination (RFE):**
  - Iteratively removes less important features using a base estimator (e.g., linear regression).
  - Provided some improvement, but was sensitive to collinearity and did not outperform the baseline.

- **Tree-Based Feature Importance (Random Forest):**
  - Captures non-linear relationships and feature interactions.
  - Delivered better results than univariate and RFE, but still not optimal for this dataset.

- **Sequential Forward Selection (SFS):**
  - Wrapper method that iteratively adds features based on model performance improvement (using cross-validated RMSE).
  - Consistently produced the lowest RMSE and highest R² in notebook experiments.
  - Able to capture complex, non-linear relationships and feature interactions.

**Tradeoff & Decision:**

After extensive experimentation in the notebook, SFS was chosen for integration into the modular pipeline because it:
- Provided the best balance of predictive accuracy and feature interpretability.
- Is robust to multicollinearity and can adapt to different model types.
- Integrates seamlessly with scikit-learn pipelines and cross-validation, supporting reproducible and automated workflows.

While SFS is more computationally intensive than filter methods, its performance gains and flexibility justified its use as the default feature selection strategy in this project.

---

## Support

- Email: pesmithiii7@gmail.com
- Documentation: [Milestone 1]() | [Milestone 2]() | [Milestone 3]()
- Repository: [GitHub](https://github.com/PESIII23/real-estate-price-prediction)
