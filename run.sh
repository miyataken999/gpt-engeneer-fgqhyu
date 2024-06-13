#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the application
python app/app.py &

# Run the tests
pytest tests/test_app.py
