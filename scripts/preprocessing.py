"""
Preprocess data
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_and_clean_data(filepath: str):
    """
    Load and clean data from a CSV file.

    Parameters:
    filepath (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Cleaned DataFrame.
    """
    # Load data
    df = pd.read_csv(filepath)

    # Drop rows with missing values
    df.dropna(inplace=True)

    df.drop_duplicates(inplace=True)

    # df.fillna(0, inplace=True)

    return df


def normalize_features(
    df: pd.DataFrame, target_feature="hydrogen_price", drop_features=None
):
    """
    Normalize features in the DataFrame.
    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    target_feature (str): The target feature to exclude from normalization.
    drop_features (list): List of features to drop from the DataFrame.
    Returns:
    scaled_features (np.ndarray): Scaled features.
    target (pd.Series): Target variable.
    scaler (StandardScaler): Fitted scaler object.
    """
    scaler = StandardScaler()
    target = df[target_feature]
    features = df.drop(
        columns=[target_feature, *drop_features] if drop_features else [target_feature]
    )
    scaled_features = scaler.fit_transform(features)

    return scaled_features, target, scaler
