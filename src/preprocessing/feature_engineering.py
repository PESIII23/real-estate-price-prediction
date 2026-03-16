"""
Transform data elements for EDA readiness...
"""
import pandas as pd
import numpy as np
import logging

class FeatureEngineer:
    _logger = logging.getLogger(__name__ + "." + __qualname__) 

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply feature engineering methods to the transformed data source"""
    transform = FeatureEngineer(df)
    return transform.get_dataframe()