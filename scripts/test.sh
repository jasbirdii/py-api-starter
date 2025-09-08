#!/bin/bash

# Testing script
set -e

echo "🧪 Running tests..."

# Run pytest
echo "🔬 Running pytest..."
poetry run pytest -v --cov=app --cov-report=html --cov-report=term-missing

echo "✅ Tests completed!"
echo "📊 Coverage report generated in htmlcov/index.html"
