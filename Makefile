.PHONY: help dev dev-frontend dev-backend build build-frontend build-backend test test-frontend test-backend coverage lint lint-frontend lint-backend format typecheck setup update-deps clean clean-all

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ============================================================================
# Development Commands
# ============================================================================

dev: ## Start both frontend and backend in development mode
	@echo "Starting frontend and backend..."
	@make -j2 dev-frontend dev-backend

dev-frontend: ## Start only frontend
	@echo "Starting frontend on http://localhost:5173"
	cd frontend && npm run dev

dev-backend: ## Start only backend
	@echo "Starting backend on http://localhost:8000"
	@echo "API docs available at http://localhost:8000/docs"
	cd backend && conda run -n Rag python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# ============================================================================
# Build Commands
# ============================================================================

build: build-frontend build-backend ## Build both frontend and backend

build-frontend: ## Build frontend for production
	@echo "Building frontend..."
	cd frontend && npm run build

build-backend: ## Build backend (prepare for deployment)
	@echo "Backend is ready for deployment (no build step needed)"

# ============================================================================
# Testing Commands
# ============================================================================

test: test-frontend test-backend ## Run all tests

test-frontend: ## Run frontend tests
	@echo "Running frontend tests..."
	cd frontend && npm run test

test-backend: ## Run backend tests
	@echo "Running backend tests..."
	cd backend && conda run -n reflection-agent pytest

coverage: ## Generate coverage reports
	@echo "Generating coverage reports..."
	cd frontend && npm run test:coverage || true
	cd backend && conda run -n reflection-agent pytest --cov=app --cov-report=html --cov-report=term || true

# ============================================================================
# Code Quality Commands
# ============================================================================

lint: lint-frontend lint-backend ## Check code quality (frontend + backend)

lint-frontend: ## Check frontend code with Biome
	@echo "Linting frontend..."
	cd frontend && npm run lint

lint-backend: ## Check backend code
	@echo "Linting backend..."
	cd backend && conda run -n reflection-agent pytest --flake8 || true

format: ## Format all code
	@echo "Formatting code..."
	cd frontend && npm run format
	cd backend && conda run -n reflection-agent black . || true

typecheck: ## Run TypeScript type checking
	@echo "TypeScript type checking..."
	cd frontend && npm run typecheck

# ============================================================================
# Setup Commands
# ============================================================================

setup: ## Set up the project from scratch
	@echo "Setting up Reflection Agent project..."
	@$(MAKE) _check-prerequisites
	@echo "Setting up backend..."
	cd backend && conda env create -f environment.yml || conda env update -f environment.yml
	@echo "Setting up frontend..."
	cd frontend && npm install
	@echo ""
	@echo "✓ Setup complete!"
	@echo ""
	@echo "To start development:"
	@echo "  make dev"
	@echo ""
	@echo "To activate the conda environment:"
	@echo "  conda activate reflection-agent"

update-deps: ## Update all dependencies
	@echo "Updating dependencies..."
	cd backend && conda env update -f environment.yml --prune
	cd frontend && npm update

# ============================================================================
# Clean Commands
# ============================================================================

clean: ## Remove build artifacts
	@echo "Cleaning build artifacts..."
	rm -rf frontend/dist frontend/build
	rm -rf backend/__pycache__ backend/app/__pycache__
	rm -rf backend/.pytest_cache backend/htmlcov backend/.coverage
	find backend -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find backend -type f -name "*.pyc" -delete
	@echo "✓ Clean complete"

clean-all: clean ## Remove all generated files and dependencies
	@echo "Removing all dependencies and generated files..."
	rm -rf frontend/node_modules
	rm -rf frontend/.biome-cache
	@echo "⚠️  To remove the conda environment, run: conda env remove -n reflection-agent"
	@echo "✓ Clean-all complete"

# ============================================================================
# Internal Commands
# ============================================================================

_check-prerequisites:
	@echo "Checking prerequisites..."
	@command -v node >/dev/null 2>&1 || { echo "❌ Node.js is not installed. Please install Node.js 18+"; exit 1; }
	@command -v conda >/dev/null 2>&1 || { echo "❌ Conda is not installed. Please install Miniconda or Anaconda"; exit 1; }
	@command -v make >/dev/null 2>&1 || { echo "❌ Make is not installed. Please install GNU Make"; exit 1; }
	@echo "✓ All prerequisites are installed"
