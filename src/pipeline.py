"""
Real Estate Price Prediction

Orchestrates the end-to-end credit risk analysis workflow:
    1. Data ingestion from imported data file
    2. Exploratory Data Analysis
    3. Data transformations (data value mods, log transforms)
    4. Feature engineering
    5. Export modeling-ready DataFrame

Usage:
    CLI:      python -m src.pipeline
    Python:   from src.pipeline import run_pipeline; full_df, modeling_df = run_pipeline()
"""
import pandas as pd
from pathlib import Path
from src.preprocessing import data_preparation, data_transformation, feature_engineering
from src.viz import plotting

PROJECT_ROOT = Path('/Users/phillipsmith/Desktop/pythonProjects/real-estate-price-prediction')

class Paths:
    RAW_FILE = PROJECT_ROOT / 'src' / 'data' / 'raw' / 'Dataset Project 2.xlsx'
    RAW_PARQUET = PROJECT_ROOT / 'src' / 'data' / 'raw' / 'dataset.parquet'
    # MODELING_DATA = PROJECT_ROOT / 'src' / 'data' / 'processed' / 'modeling_df.parquet'

def run_pipeline(verbose: bool = True) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Execute the full pipeline. Returns (full_df, modeling_df).
        """
        log = print if verbose else lambda *args, **kwargs: None
        
        """
        HEADER
        """
        print()
        log("=" * 60)
        log("REAL ESTATE PRICE PREDICTION PIPELINE")
        log("=" * 60)
        
        """
        STAGE 1: INGEST DATA
        """
        log("\n[1/7] LOADING DATA FROM SOURCE FILE...\n")
        df = pd.read_excel(Paths.RAW_FILE, header=1)
        df.to_parquet(Paths.RAW_PARQUET, engine='fastparquet')
        log(f"      Loaded {len(df):,} records.")
        log(f"      DataFrame shape: {df.shape}\n")
        print(df.head())
        
        """
        STAGE 2: CLEAN DATA
        """
        log("\n[2/7] CLEANING DATA...\n")
        df = pd.read_parquet(Paths.RAW_PARQUET, engine='fastparquet')
        df_cleaned = data_preparation.clean_data(df)
        missing = data_preparation.CleanData(df_cleaned).is_missing_vals()
        if missing:
            log("      WARNING: Missing values detected in cleaned data.\n")
            # apply imputation or other missing data approaches
        log(f"      Data is cleaned.\n")
        print(df_cleaned.describe())

        """
        STAGE 3: TRANSFORM DATA
        """
        log("\n[3/7] TRANSFORMING DATA...\n")
        df_transformed = data_transformation.transform_data(df_cleaned)
        log("      Data is transformed.\n")
        print(df_transformed.head())

        """
        STAGE 4: EXPLORATORY DATA ANALYSIS
        """
        log("\n[4/7] PERFORMING EDA...\n")
        df_correlated = plotting.explore_data(df_transformed)
        log("      Generated EDA plots. Please see docs/eda_*.\n")
        print(df_correlated.columns)

        """
        STAGE 5: FEATURE ENGINEERING
        """
        log("\n[5/7] ENGINEERING FEATURES...\n")
        # full_df, modeling_df = engineer_features(df, n_neighbors=5)
        # log(f"      Created {len(modeling_df.columns)} features")
        
        # # Stage 4: Export Modeling Dataframe
        # log("\n[4/5] EXPORTING MODELING DATA...")
        # Paths.MODELING_DATA.parent.mkdir(parents=True, exist_ok=True)
        # modeling_df.to_parquet(Paths.MODELING_DATA, engine='fastparquet', index=False)

        # # Stage 5: Apply Logistic Regression
        # log("\n[5/5] APPLYING LOGISTIC REGRESSION TO MODELING DATA...")
        # classifier = CreditRiskClassifier(test_size=0.5, random_state=24)
        # classifier.fit_and_evaluate(modeling_df)
        # log(f"      Confusion Matrix:\n{classifier.cnf_matrix}")
        # log(f"      AUC Score: {classifier.get_auc_score():.4f}")
        # log(f"\n{classifier.get_classification_report()}")
        
        # # Display plots
        # classifier.evaluate(plot=True)
        # classifier.plot_roc_curve()
        
        # Summary
        # log("\n" + "=" * 60)
        # log("PIPELINE COMPLETE")
        # log("=" * 60)
        # log(f"\nFull DataFrame:     {full_df.shape}")
        # log(f"Modeling DataFrame: {modeling_df.shape}")
        
        return


if __name__ == "__main__":
    run_pipeline(verbose=True)