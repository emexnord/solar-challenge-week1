import os
import pandas as pd
import numpy as np
import pytest

# Assume your main script is scripts/malawi_eda.py and you refactored key logic into functions.
# For example, load_data(), clean_data(), export_data(), etc.

from scripts.malawi_eda import load_data, clean_data, export_cleaned_data

def test_load_data():
    df = load_data("../data/Solar-Measurements_Malawi_Chileka_WB-ESMAP_Raw_00.dat")
    assert isinstance(df, pd.DataFrame)
    assert '"TIMESTAMP"' in df.columns
    assert len(df) > 0

def test_clean_data():
    df = load_data("../data/Solar-Measurements_Malawi_Chileka_WB-ESMAP_Raw_00.dat")
    df_cleaned = clean_data(df)
    # Check no outlier z-score > 3
    cols_to_check = [
        '"GHI_Avg"', '"DNI_Avg"', '"DNICalc_Avg"', '"Temp_Avg"', '"WS_Avg"',
    ]
    from scipy.stats import zscore
    z_scores = df_cleaned[cols_to_check].apply(zscore)
    assert not (z_scores.abs() > 3).any(axis=None)
    # Check no missing values in checked columns
    assert df_cleaned[cols_to_check].isna().sum().sum() == 0

def test_export_cleaned_data(tmp_path):
    df = load_data("../data/Solar-Measurements_Malawi_Chileka_WB-ESMAP_Raw_00.dat")
    df_cleaned = clean_data(df)
    output_file = tmp_path / "malawi_clean.csv"
    export_cleaned_data(df_cleaned, output_file)
    assert os.path.exists(output_file)
    # Check exported file can be read
    df_loaded = pd.read_csv(output_file)
    assert len(df_loaded) == len(df_cleaned)
