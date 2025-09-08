#!/bin/bash

# Linting and formatting script
set -e

echo "🔍 Running linter and formatter..."

# Run ruff for linting and formatting
echo "📝 Running ruff..."
poetry run ruff check .
poetry run ruff format --check .

# Run mypy for type checking
echo "🔬 Running mypy..."
poetry run mypy .

echo "✅ All checks passed!"
