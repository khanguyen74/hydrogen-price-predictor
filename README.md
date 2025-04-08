# Hydrogen Price Prediction - Junior AI Engineer Take-Home Project

This project tackles a regression task to predict future hydrogen market prices using historical data and related features such as energy costs, government policy scores, and demand fluctuations.

The project includes:

Data preprocessing and exploratory data analysis (EDA) (Jupyter Notebook)

Model training and evaluation (Linear Regression, Random Forest, Decision Tree) (Jupyter Notebook)

A FastAPI-based API to serve predictions

Pickle-based model and scaler serialization

## Project Structure

```plaintext
hydrogen-price-predictor/
├── app/
│   └── main.py
├── data/
│   └── hydrogen_prices.csv
├── models/
│   ├── model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── hydrogren_prices_analysis.ipynb
├── scripts/
│   ├── genearate_dataset.py
│   ├── model_training.py
│   └── preprocessing.py
├── Makefile
├── README.md
└── requirements.txt
```

## Dataset

As no real-world dataset was provided with the problem statement, a synthetic dataset was generated to simulate historical hydrogen market prices along with key influencing factors.

### Data Generation

A Python script was used to create 500 weekly records starting from January 2016. The features were designed to reflect realistic variations in the hydrogen energy market:

- `energy_cost`: Simulated using a normal distribution centered around $50 with slight variation to mimic fluctuating energy prices.

- `gov_policy_score`: A score between 0 and 10 indicating the favorability of government policies, with higher scores implying more supportive conditions for hydrogen production.

- `demand_index`: A normalized index representing market demand, centered around 1.0, with random fluctuations to simulate real-world demand variability.

- `hydrogen_price`: The target variable, computed as a linear combination of the above features plus some noise to simulate realistic randomness.

## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## API (Run the FastAPI server locally)

Make sure you have installed the required packages and have the model and scaler files in the `models/` directory.

### Run the FastAPI server manually

```bash
fastapi run app/main.py
```

The server will be running on port 8000 by default

### Sample request

Endpoint: POST /predict

Payload:

```json
{
  "energy_cost": 50.0,
  "gov_policy_score": 10.0,
  "demand_index": 1.25
}
```

```bash
curl -X POST localhost:8000/predict -H "Content-Type: application/json" \
-d '{
    "energy_cost": 50.0,
    "gov_policy_score": 10.0,
    "demand_index": 2.25
}'

```

Response:

```json
{
  "prediction": 41.6522452965522
}
```

Endpoint: POST /predict_batch

```json
[
  {
    "energy_cost": 100.0,
    "gov_policy_score": 5.0,
    "demand_index": 1.25
  },
  {
    "energy_cost": 84.35,
    "gov_policy_score": 9.0,
    "demand_index": 2.25
  }
]
```

Response:

```json
{
  "predictions": [72.6568118223029, 75.43057271065331]
}
```

## Train the Model

The model can be trained using this command:

```bash
python scripts/model_training.py
```

After train successfully, the model and scaler will be saved in the `model/` directory. And will be used by the FastAPI server.

## Makefile Usage

This project includes a Makefile for easy execution of common tasks. You can use the following commands:

### Setup Environment

```bash
make setup_env
```

Creates a virtual environment in .venv and installs dependencies listed in requirements.txt.

> Note: Run this once when setting up the project for the first time.

### Reinstall Dependencies

```bash
make install
```

Installs project dependencies into an already-created virtual environment.

### Generate Dataset

```bash
make generate
```

### Train model

```bash
make train

```

### Run FastAPI server

```bash
make api
```

### Start Jupyter Notebook

```bash
make notebook
```

### Clean Up

```bash
make clean
```
