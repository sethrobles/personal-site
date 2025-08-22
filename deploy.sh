#!/bin/bash

# Deployment script for Seth Robles Portfolio
# This script helps with common deployment tasks

set -e

echo "🚀 Seth Robles Portfolio - Deployment Script"
echo "=============================================="

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository. Please run this script from the project root."
    exit 1
fi

# Function to check deployment status
check_deployment() {
    echo "📋 Checking deployment status..."

    # Check if render.yaml exists
    if [ -f "render.yaml" ]; then
        echo "✅ render.yaml found"
    else
        echo "❌ render.yaml not found"
    fi

    # Check if requirements.txt exists
    if [ -f "requirements.txt" ]; then
        echo "✅ requirements.txt found"
    else
        echo "❌ requirements.txt not found"
    fi

    # Check if Procfile exists
    if [ -f "Procfile" ]; then
        echo "✅ Procfile found"
    else
        echo "❌ Procfile not found"
    fi

    # Check if app.py exists
    if [ -f "app.py" ]; then
        echo "✅ app.py found"
    else
        echo "❌ app.py not found"
    fi

    # Check if portfolio template exists
    if [ -f "templates/portfolio.html" ]; then
        echo "✅ portfolio.html template found"
    else
        echo "❌ portfolio.html template not found"
    fi
}

# Function to prepare for deployment
prepare_deployment() {
    echo "🔧 Preparing for deployment..."

    # Check git status
    if [ -n "$(git status --porcelain)" ]; then
        echo "⚠️  You have uncommitted changes. Please commit or stash them first."
        git status --short
        echo ""
        read -p "Do you want to continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Deployment cancelled."
            exit 1
        fi
    fi

    # Check if virtual environment exists
    if [ -d "venv" ]; then
        echo "✅ Virtual environment found"
    else
        echo "⚠️  Virtual environment not found. Creating one..."
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    fi
}

# Function to test locally
test_local() {
    echo "🧪 Testing application locally..."

    if [ -d "venv" ]; then
        source venv/bin/activate
    fi

    echo "Starting Flask application on port 5001..."
    echo "Press Ctrl+C to stop the server"
    echo ""

    python app.py
}

# Function to deploy to Render
deploy_render() {
    echo "🚀 Deploying to Render..."

    # Check if we have a remote origin
    if ! git remote get-url origin &> /dev/null; then
        echo "❌ No git remote 'origin' found."
        echo "Please add your Render repository as origin:"
        echo "git remote add origin <your-render-repo-url>"
        exit 1
    fi

    # Get current branch
    current_branch=$(git branch --show-current)
    echo "Current branch: $current_branch"

    # Push to origin
    echo "Pushing to origin/$current_branch..."
    git push origin $current_branch

    echo "✅ Deployment initiated!"
    echo "Check your Render dashboard for deployment status."
}

# Function to show help
show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  check     - Check deployment readiness"
    echo "  prepare   - Prepare for deployment"
    echo "  test      - Test application locally"
    echo "  deploy    - Deploy to Render"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 check     # Check if everything is ready for deployment"
    echo "  $0 test      # Test the application locally"
    echo "  $0 deploy    # Deploy to Render"
}

# Main script logic
case "${1:-help}" in
    "check")
        check_deployment
        ;;
    "prepare")
        prepare_deployment
        ;;
    "test")
        test_local
        ;;
    "deploy")
        prepare_deployment
        deploy_render
        ;;
    "help"|*)
        show_help
        ;;
esac
