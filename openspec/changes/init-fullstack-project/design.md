# Design: Full-Stack Project Initialization

## Architecture Overview

```
project-root/
├── frontend/                 # React + TypeScript + Vite
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API query functions (used by TanStack Query)
│   │   ├── types/           # TypeScript type definitions
│   │   ├── App.tsx          # Root application component
│   │   └── main.tsx         # Application entry point
│   ├── public/              # Static assets
│   ├── biome.json           # Biome configuration
│   ├── tsconfig.json        # TypeScript configuration
│   ├── vite.config.ts       # Vite build configuration
│   ├── package.json         # Frontend dependencies
│   └── index.html           # HTML entry point
│
├── backend/                 # FastAPI + Python
│   ├── app/
│   │   ├── api/             # API route handlers
│   │   │   └── v1/          # API versioning
│   │   ├── core/            # Core application config
│   │   ├── models/          # Database models (future)
│   │   ├── schemas/         # Pydantic models for validation
│   │   ├── services/        # Business logic layer
│   │   └── main.py          # FastAPI application entry
│   ├── tests/               # Backend tests
│   ├── environment.yml      # Conda environment specification
│   └── pyproject.toml       # Python dependencies (PEP 518)
│
├── Makefile                 # Unified command interface
├── .gitignore              # Git ignore patterns
└── README.md               # Project documentation
```

## Technology Choices

### Frontend Stack
- **React 18+**: Modern React with hooks and concurrent features
- **TypeScript 5+**: Type safety and enhanced developer experience
- **Vite 5+**: Fast dev server, optimized builds, native ESM
- **Biome**: Ultra-fast linter/formatter replacing ESLint+Prettier
- **@tanstack/react-query**: Data synchronization and state management with automatic caching, refetching, and background updates

### Backend Stack
- **FastAPI 0.104+**: Modern async framework with automatic OpenAPI
- **Python 3.11+**: Latest stable Python with performance improvements
- **Pydantic v2**: Data validation using Python type annotations
- **UVicorn**: ASGI server for production deployment
- **pytest + pytest-asyncio**: Async testing support

### Development Tools
- **Conda**: Python environment management and reproducibility
- **Make**: Unified command interface for all operations
- **Git hooks**: Pre-commit hooks for code quality (optional future)

## Design Decisions

### 1. Monorepo Structure
**Decision**: Use single repository with separate frontend/backend directories

**Rationale**:
- Simplified development with unified tooling (Make)
- Easier code sharing and type synchronization
- Lower operational overhead for small to medium teams
- Frontend and backend can be deployed independently

**Trade-offs**:
- Tighter coupling than separate repos
- Shared git history may grow large

### 2. Biome over ESLint+Prettier
**Decision**: Use Biome for frontend linting and formatting

**Rationale**:
- 100x faster than ESLint+Prettier
- Single tool for both linting and formatting
- Native TypeScript support
- ESLint compatibility mode for migration

**Trade-offs**:
- Newer ecosystem with fewer plugins
- May not support all ESLint rules

### 3. Conda over venv
**Decision**: Use Conda for Python environment management

**Rationale**:
- Better dependency resolution for scientific packages
- Easy environment reproducibility via environment.yml
- Non-Python dependencies support (future-proofing)
- Cross-platform consistency

**Trade-offs**:
- Heavier than venv
- Slower environment creation

### 4. Make as Unified Interface
**Decision**: Use Makefile with targets for all common operations

**Rationale**:
- Familiar interface for most developers
- Easy to document and discover commands
- Platform-independent (works on Unix-like systems)
- Simple to extend with new commands

**Trade-offs**:
- Windows users need WSL or alternative
- Not as featureful as dedicated task runners

### 5. API Communication Pattern
**Decision**: Use TanStack Query (React Query) with fetch for data fetching and state management

**Rationale**:
- Automatic caching and background refetching reduces server load
- Built-in loading, error, and data states eliminate boilerplate
- TypeScript-first design with excellent type inference
- Automatic retries and request deduplication
- Window focus refocusing keeps data fresh automatically
- No need for separate state management library for server state
- Optimistic updates and mutation handling built-in
- DevTools for debugging queries and cache state

**Trade-offs**:
- Additional library to learn (but follows standard React patterns)
- Bundle size (~13kb minzipped) is offset by reduced boilerplate code
- Overkill for simple projects but scales perfectly with complexity
- Uses fetch or Axios under the hood (we'll use fetch for zero dependencies)

## Development Workflow

### Initial Setup
```bash
# Create and activate conda environment
conda env create -f backend/environment.yml
conda activate reflection-agent

# Install frontend dependencies
cd frontend && npm install
```

### Development
```bash
make dev          # Start frontend (port 5173) + backend (port 8000)
make dev-frontend # Start only frontend
make dev-backend  # Start only backend
```

### Code Quality
```bash
make lint         # Check all code (Biome + Python tools)
make lint-frontend
make lint-backend
make format       # Auto-format all code
```

### Testing
```bash
make test         # Run all tests
make test-frontend
make test-backend
make coverage     # Generate coverage reports
```

### Building
```bash
make build        # Production builds for both
make build-frontend
make build-backend
```

## Future Considerations

### Phase 2 Additions
- Database integration (PostgreSQL + SQLAlchemy)
- Authentication (JWT + refresh tokens with TanStack Query integration)
- Client-side state management (Zustand for global UI state)
- API versioning strategy
- Docker containerization

### Performance Optimizations
- Frontend code splitting and lazy loading
- Backend caching layer (Redis)
- API response compression
- Static asset CDN deployment

### Developer Experience
- Hot module replacement in development
- TypeScript type sharing between frontend/backend
- API client generation from OpenAPI spec
- Pre-commit hooks with Husky
