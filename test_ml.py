import pytest
import os
import pandas as pd
import numpy as np
from ml import model
from sklearn.ensemble import RandomForestClassifier


@pytest.fixture(scope="session")
def test_data_path():
    test_path = os.getcwd()
    test_data_path = os.path.join(test_path, "data", "census.csv")
    df = pd.read_csv(test_data_path)
    return df

def test_algorithm():
    """
    # If the ML model uses the expected algorithm.
    """
    X_train = np.random.rand(100, 25)
    y_train = np.random.randint(2, size=100)

    model_output = model.train_model(X_train, y_train)

    assert isinstance(model_output, RandomForestClassifier)

def test_loaded():
    """
    Test data was successfully loaded.
    """
    data_path = "data/census.csv"
    df = pd.read_csv(data_path)

    assert not df.empty, "Data not loaded successfully."

def test_data():
    """
    # Test to make sure the dataset has enough data for project
    """
    data_path = "data/census.csv"
    df = pd.read_csv(data_path)

    assert df.shape[0] > 10000
