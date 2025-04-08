from os import path
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

from preprocessing import load_and_clean_data, normalize_features


def train():
    """This function trains a model by first loading and cleaning the data,
    normalizing the features, splitting the data into training and testing sets,
    """
    filename = path.join(path.dirname(__file__), "../data/hydrogen_prices.csv")
    df = load_and_clean_data(filename)
    X, y, scaler = normalize_features(
        df=df, drop_features=["date", "average_temperature"]
    )

    # Split the data into training and testing sets

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print(f"MAE: {mean_absolute_error(y_test, preds):.4f}")
    print(f"RMSE: {mean_squared_error(y_test, preds):.4f}")
    print(f"R²: {r2_score(y_test, preds):.4f}")

    model_path = path.join(path.dirname(__file__), "../models")
    # Save model and scaler
    with open(path.join(model_path, "model.pkl"), "wb") as f:
        pickle.dump(model, f)
        print(f"Model saved to {model_path}")

    with open(path.join(model_path, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)
        print(f"Scaler saved to {model_path}")


if __name__ == "__main__":
    train()
