# Project Scaffold: ML Pipeline

Steps to recreate this project directory from scratch.

---

## 1. Create the directory structure

```
<project-root>/
├── .gitignore
├── README.md
├── requirements.txt
├── ai_agent_files/
│   ├── common.md
│   └── git.md
├── docs/
└── src/
    ├── __init__.py
    ├── preprocessing/
    │   ├── __init__.py
    │   ├── data_prep.py
    │   └── feature_engineering.py
    ├── models/
    │   ├── __init__.py
    │   └── model.py
    ├── notebooks/
    │   └── price_prediction_model.ipynb
    ├── data/
    │   ├── raw/
    │   └── processed/
    └── viz/
        ├── __init__.py
        └── plotting.py
```

## 2. File purposes

- **All `.py` files** — created empty (no boilerplate, no docstrings, no classes).
- **All `__init__.py` files** — created empty.
- **`README.md`** — use the standard project README template (see section 6).
- **`requirements.txt`** — Python dependencies (pandas, numpy, matplotlib, seaborn, openpyxl, scikit-learn).
- **`price_prediction_model.ipynb`** — created as a blank Jupyter Notebook (no cells).
- **`docs/`** — deliverable documents (EDA findings, ML template).

### `src/preprocessing/`

| File | Purpose |
|------|---------|
| `data_prep.py` | NaN removal, duplicate handling, outlier removal, train/test splitting |
| `feature_engineering.py` | Variable selection, X/y separation, scaling (StandardScaler, MinMaxScaler) |

### `src/models/`

| File | Purpose |
|------|---------|
| `model.py` | Model definitions (Linear Regression, Random Forest, Lasso, Ridge), training, evaluation metrics, model comparison, back-testing across split ratios |

### `src/viz/`

| File | Purpose |
|------|---------|
| `plotting.py` | Reusable chart functions — bar charts, scatter plots, histplots, correlation heatmaps |

## 3. `__init__.py` placement rules

Add an empty `__init__.py` to every directory under `src/` that contains importable Python modules:

- `src/`
- `src/preprocessing/`
- `src/models/`
- `src/viz/`

Do **not** add `__init__.py` to:

- `src/data/` (holds data files, not Python modules)
- `src/notebooks/` (holds notebooks, not Python modules)
- `ai_agent_files/` (holds reference docs, not Python modules)
- `docs/` (holds deliverable documents, not Python modules)

## 4. `.gitignore`

Create a `.gitignore` at the project root with the following:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
build/
dist/
*.egg-info/
*.egg

# Virtual environments
.venv/
venv/
env/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# mypy cache
.mypy_cache/

# pytest cache
.pytest_cache/

# Ruff cache
.ruff_cache/

# macOS
.DS_Store

# IDE
.idea/
.vscode/

# Data files (keep structure, ignore large files)
src/data/raw/*.xlsx
src/data/raw/*.csv
src/data/processed/*.parquet
src/data/processed/*.csv

# Environment variables
.env
```

## 5. `requirements.txt`

Create a `requirements.txt` at the project root with:

```
pandas
numpy
matplotlib
seaborn
openpyxl
scikit-learn
```

## 6. `README.md` template

Use the following template for `README.md`, adapting the project name, description, structure, stages, features, and tools to fit the specific project:

```markdown
# <Project Name>

<One-sentence description of the project.>

---

## Project Structure

<Tree view of src/ showing directories and files with inline comments.>

---

## Quick Start

**1. Clone the repository:**
git clone <repo-url>
cd <project-name>

**2. Create a virtual environment:**
python -m venv .venv
source .venv/bin/activate

**3. Install dependencies:**
pip install -r requirements.txt

**4. Run the notebook:**
Place the source data file in src/data/raw/, then open the notebook.

---

## Pipeline Stages

| Stage | Description |
|-------|-------------|
| **1. Data Loading** | ... |
| **2. EDA** | ... |
| **3. Data Wrangling** | ... |
| **4. Feature Engineering** | ... |
| **5. Modeling** | ... |
| **6. Evaluation** | ... |

---

## Key Features

- **Feature 1** – Description
- **Feature 2** – Description

---

## Tools & Libraries

- Python 3.x+
- List each library and its purpose

---

## Support

- Email: pesmithiii7@gmail.com
- Repository: [GitHub](<repo-url>)
```

## 7. Summary of steps in order

1. Create the project root directory.
2. Initialize git (`git init`).
3. Create `README.md` using the template from section 6, adapted for the project.
4. Create `requirements.txt` with Python dependencies.
5. Create `ai_agent_files/` with `common.md` and `git.md` reference docs.
6. Create `docs/` for deliverable documents.
7. Create `src/` and all subdirectories (`preprocessing/`, `models/`, `notebooks/`, `data/raw/`, `data/processed/`, `viz/`).
8. Create all `.py` files — every file is empty, no boilerplate.
9. Create empty `__init__.py` in `src/`, `src/preprocessing/`, `src/models/`, and `src/viz/`.
10. Create a blank Jupyter Notebook at `src/notebooks/price_prediction_model.ipynb`.
11. Create `.gitignore` at the project root with the contents from step 4.
