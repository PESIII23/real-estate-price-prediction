"""
Model definitions (Linear Regression, Random Forest, Lasso, Ridge), training, evaluation, and comparison.
"""
import pandas as pd
import numpy as np
import logging

from src.viz import model_plots
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class Regression:
    _logger = logging.getLogger(__name__ + "." + __qualname__)

    def __init__(self, df: pd.DataFrame, test_size, random_state):
        self.df = df.copy()
        self.test_size = test_size
        self.random_state = random_state


    def linear_regression(self, X, y):
        model = LinearRegression(fit_intercept=True)

        X_train, X_test, y_train, y_test = train_test_split(
            X, 
            y, 
            test_size=self.test_size,
            random_state=self.random_state)
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"      LINEAR REGRESSION RESULTS:\n")
        print(f"      INTERCEPT: {model.intercept_}")
        print(f"      COEFFICIENTS: {len(model.coef_)}")
        return y_pred, y_test, X_test, model, X
    
    # def random_forest(self, df, )

    def print_results(self, y_pred, y_test, X_test, model):
        print(f"      MEAN ABSOLUTE ERROR: {mean_absolute_error(y_test, y_pred)}")
        print(f"      MEAN SQUARED ERROR: {mean_squared_error(y_test,y_pred)}")
        print(f"      ROOT MEAN SQUARED ERROR: {np.sqrt(mean_squared_error(y_test,y_pred))}")
        print(f"      R-SQUARED VALUE: {model.score(X_test,y_test)}")

def apply_regression(df):
    """Apply regression methods to the modeling data source"""
    regression = Regression(df, test_size=.2, random_state=3)
    X = df.drop(columns=[
        'price',
        'rad_3',
        'population_distribution_popul_flip_log',
        'crime_rate_per_capita_crim_log'
        ])
    y = df['price']

    # LINEAR REGRESSION
    y_pred, y_test, X_test, model, X = regression.linear_regression(X, y)
    regression.print_results(y_pred, y_test, X_test, model)
    linear_reg_plots = model_plots.ModelPlots(y_pred=y_pred, y_test=y_test, X_test=X_test, X=X)
    linear_reg_plots.plot_linearity_and_residuals(model="linear_reg")
    linear_reg_plots.plot_distribution(model="linear_reg")
    linear_reg_plots.plot_pairplot(model="linear_reg")

    # RANDOM FOREST
    # linear_reg_plots.plot_input_with_target("randon_for")

    # LASSO REGRESSION

    # RIDGE REGRESSION
    return