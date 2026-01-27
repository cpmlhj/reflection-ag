# Reflection Agent

A modern full-stack web application built with React + TypeScript (frontend) and FastAPI + Python (backend).

## Tech Stack

### Frontend
- **React 18+** - Modern React with hooks and concurrent features
- **TypeScript 5+** - Type safety and enhanced developer experience
- **Vite 5+** - Fast dev server and optimized builds
- **Biome** - Ultra-fast linter and formatter
- **TanStack Query** - Data synchronization and state management

### Backend
- **FastAPI 0.104+** - Modern async framework with automatic OpenAPI
- **Python 3.11+** - Latest stable Python with performance improvements
- **Pydantic v2** - Data validation using Python type annotations
- **UVicorn** - ASGI server for production deployment
- **pytest** - Async testing support

## Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js 18+** and npm
- **Conda** (Miniconda or Anaconda)
- **Make** (GNU Make)

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd reflection-agent

# Run the setup command
make setup
```

### 2. Development

```bash
# Start both frontend and backend
make dev

# Start only frontend
make dev-frontend

# Start only backend
make dev-backend
```

The frontend will be available at `http://localhost:5173`
The backend will be available at `http://localhost:8000`
Backend API docs at `http://localhost:8000/docs`

## Available Commands

### Development
- `make dev` - Start both frontend and backend in development mode
- `make dev-frontend` - Start only frontend
- `make dev-backend` - Start only backend

### Building
- `make build` - Build both frontend and backend for production
- `make build-frontend` - Build only frontend
- `make build-backend` - Build only backend

### Testing
- `make test` - Run all tests
- `make test-frontend` - Run frontend tests
- `make test-backend` - Run backend tests
- `make coverage` - Generate coverage reports

### Code Quality
- `make lint` - Check code quality (frontend + backend)
- `make lint-frontend` - Check frontend code with Biome
- `make lint-backend` - Check backend code
- `make format` - Format all code
- `make typecheck` - Run TypeScript type checking

### Setup & Maintenance
- `make setup` - Set up the project from scratch
- `make update-deps` - Update all dependencies
- `make clean` - Remove build artifacts
- `make clean-all` - Remove all generated files and dependencies
- `make help` - Show all available commands

## Project Structure

```
.
├── frontend/          # React + TypeScript + Vite
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API query functions
│   │   ├── types/         # TypeScript type definitions
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── biome.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── backend/           # FastAPI + Python
│   ├── app/
│   │   ├── api/          # API route handlers
│   │   ├── core/         # Core configuration
│   │   ├── schemas/      # Pydantic models
│   │   ├── services/     # Business logic
│   │   └── main.py
│   ├── tests/
│   ├── environment.yml
│   └── pyproject.toml
│
├── Makefile
├── .gitignore
└── README.md
```

## Development Workflow

### Frontend Development

```bash
cd frontend
npm run dev          # Start dev server
npm run build        # Build for production
npm run lint         # Check code with Biome
npm run format       # Format code with Biome
npm run typecheck    # TypeScript type checking
npm run test         # Run tests
```

### Backend Development

```bash
# Activate conda environment
conda activate reflection-agent

cd backend
python -m uvicorn app.main:app --reload  # Start dev server
pytest                                      # Run tests
```

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Troubleshooting

### Conda Environment Issues

```bash
# Remove existing environment
conda env remove -n reflection-agent

# Recreate from scratch
conda env create -f backend/environment.yml
```

### Frontend Build Issues

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Port Already in Use

```bash
# Check what's using the port
lsof -i :5173  # Frontend
lsof -i :8000  # Backend

# Kill the process
kill -9 <PID>
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting: `make test && make lint`
4. Submit a pull request

## License

MIT License - see LICENSE file for details
