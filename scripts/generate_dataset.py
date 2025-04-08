import pandas as pd
import numpy as np


def generate_synthetic_data(rows=500):
    np.random.seed(42)
    dates = pd.date_range(start="2018-01-01", periods=rows, freq="W")

    energy_cost = np.random.normal(loc=50, scale=10, size=rows)  # around $50
    gov_policy_score = np.random.randint(0, 11, size=rows)  # scale of 0-10
    demand_index = np.random.normal(loc=1.0, scale=0.2, size=rows)  # normalized demand
    noise = np.random.normal(0, 2, size=rows)

    # Simulate hydrogen price based on features
    hydrogen_price = (
        0.5 * energy_cost - 1.2 * gov_policy_score + 15 * demand_index + noise + 10
    )

    df = pd.DataFrame(
        {
            "date": dates,
            "energy_cost": energy_cost,
            "gov_policy_score": gov_policy_score,
            "demand_index": demand_index,
            "hydrogen_price": hydrogen_price,
        }
    )

    return df


if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv("data/hydrogen_prices.csv", index=False)
    print("Dataset generated and saved to data/hydrogen_prices.csv")
