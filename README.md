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
├── data/
│   └── hydrogen_prices.csv
├── model/
│   ├── model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── hydrogren_prices_analysis.ipynb
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## API (Run the FastAPI server locally)

Make sure you have installed the required packages and have the model and scaler files in the `models/` directory.

### Run the FastAPI server

```bash
fastapi run app/main.py
```
