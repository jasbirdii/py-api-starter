#!/bin/bash

# Development setup script
set -e

echo "🚀 Setting up development environment..."

# Check if .env exists, if not copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from example..."
    cp env.example .env
    echo "⚠️  Please edit .env file with your configuration"
fi

# Install dependencies
echo "📦 Installing dependencies..."
poetry install

# Run database migrations
echo "🗄️  Running database migrations..."
alembic upgrade head

# Start the development server
echo "🎯 Starting development server..."
echo "📚 API docs available at: http://localhost:8000/docs"
echo "🔍 Health check: http://localhost:8000/health"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
