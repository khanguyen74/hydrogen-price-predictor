VENV = .venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python
FASTAPI = $(BIN)/fastapi
PIP = $(BIN)/pip

.PHONY: all setup_env install generate train api notebook clean
setup_env:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	@echo "Environment setup complete. Activate it using 'source .venv/bin/activate'"

install:
	# only run this if you have already set up the environment
	$(PIP) install -r requirements.txt

generate:
	# Generate the dataset
	$(PYTHON) ./scripts/generate_dataset.py

train:
	$(PYTHON) ./scripts/model_training.py

api:
	$(FASTAPI) run

notebook: # Run the Jupyter notebook
	$(PYTHON) -m jupyter notebook 

clean:
	# Clean up the environment
	rm -rf .venv
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.pyo
	rm -rf *.pyd
	rm -rf *.egg-info
	rm -rf build/
	rm -rf dist/
	@echo "Clean up complete."
