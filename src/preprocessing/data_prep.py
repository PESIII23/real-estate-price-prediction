"""
Cleaning, wrangling, NaN handling, outlier removal, and train/test splitting.
"""

def clean_data(df):

    df = df.copy()

    df = df.drop([
        'Unnamed: 0'
    ], axis=1)

    df = df.rename(columns={
        'crim': 'crime_rate_per_capita (crim)',
        'zn': 'large_lot_zoning_ratio (zn)',
        'indus': 'non_retail_acre_ratio (indus)',
        'chas': 'river_boundary_flag (chas)',
        'nox': 'nox_concentration (nox)',
        'rm': 'avg_rooms_per_dwelling (rm)',
        'age': 'pre_1940_housing_ratio (age)',
        'dis': 'employment_center_distance (dis)',
        'rad': 'radial_highway_access_idx (rad)',
        'tax': 'property_tax_rate (tax)',
        'ptratio': 'pupil_teacher_ratio (ptratio)',
        'lstat': 'low_ses_population_pct (lstat)',
        'popul': 'population_distribution (popul)'
    })

    return df