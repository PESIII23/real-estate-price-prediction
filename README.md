# Real Estate Price Prediction

Predicting house prices using exploratory data analysis, data wrangling, and regression modeling in Python.

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd real-estate-price-prediction

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
real-estate-price-prediction/
├── .gitignore
├── README.md
├── requirements.txt
├── ai_agent_files/
│   ├── common.md
│   └── git.md
├── docs/                        # Deliverable documents (EDA findings, ML template)
└── src/
    ├── __init__.py
    ├── preprocessing/
    │   ├── __init__.py
    │   ├── data_prep.py             # Cleaning, wrangling, train/test split
    │   └── feature_engineering.py   # Variable selection, X/y split, scaling
    ├── models/
    │   ├── __init__.py
    │   └── model.py                 # Model definitions, training, evaluation
    ├── notebooks/
    │   └── price_prediction_model.ipynb
    ├── data/
    │   ├── raw/
    │   └── processed/
    └── viz/
        ├── __init__.py
        └── plotting.py
```

## Usage

1. Place the source Excel file in `src/data/raw/`.
2. Open `src/notebooks/price_prediction_model.ipynb`.
3. Run the notebook cells to perform EDA, data wrangling, modeling, and evaluation.
