import pandas as pd

def test_data_columns():
    df = pd.read_csv("data/iris.csv")
    # Check required columns exist
    required_cols = {"sepal_length", "sepal_width", "petal_length", "petal_width", "species"}
    assert required_cols.issubset(df.columns)

def test_no_missing_values():
    df = pd.read_csv("data/iris.csv")
    # Check for missing values
    assert df.isnull().sum().sum() == 0
