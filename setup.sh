#!/bin/bash
# setup.sh - Quick setup script for new installations

echo "🚀 Setting up AI Debugging Assistant..."

# Check Python version
python --version || { echo "❌ Python not found. Please install Python 3.8+"; exit 1; }

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install flask click rich requests pandas numpy

# Test installation
echo "🧪 Testing installation..."
python test_assistant.py

echo "✅ Setup complete! Run 'python test_assistant.py' to test."
