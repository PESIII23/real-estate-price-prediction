"""
Cleaning, wrangling, NaN handling, outlier removal, and train/test splitting.
"""

def clean_data(df):

    df = df.copy()

    df = df.drop([
        'Unnamed: 0'
    ], axis=1)

    df = df.rename(columns={
        'crim': 'crime_rate_per_capita_crim',
        'zn': 'large_lot_zoning_ratio_zn',
        'indus': 'non_retail_acre_ratio_indus',
        'chas': 'river_boundary_flag_chas',
        'nox': 'nox_concentration_nox',
        'rm': 'avg_rooms_per_dwelling_rm',
        'age': 'pre_1940_housing_ratio_age',
        'dis': 'employment_center_distance_dis',
        'rad': 'radial_highway_access_idx_rad',
        'tax': 'property_tax_rate_tax',
        'ptratio': 'pupil_teacher_ratio_ptratio',
        'lstat': 'low_ses_population_pct_lstat',
        'popul': 'population_distribution_popul'
    })

    return df
