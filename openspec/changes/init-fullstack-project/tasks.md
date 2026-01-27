# Tasks: Initialize Full-Stack Project

## Phase 1: Project Structure Setup (Can be done in parallel)

### 1.1 Create root project structure
- [ ] Create frontend/ and backend/ directories
- [ ] Create root .gitignore file (Node, Python, IDE files)
- [ ] Create root README.md with project overview and setup instructions
- [ ] Create Makefile with basic structure (help, clean targets)

**Validation**: Directories exist, README is clear, `make help` shows available commands

**Dependencies**: None

### 1.2 Initialize frontend project
- [ ] Create Vite React TypeScript project in frontend/
- [ ] Configure tsconfig.json with strict mode and path aliases
- [ ] Create directory structure (src/components, src/hooks, src/services, src/types)
- [ ] Create basic App.tsx and main.tsx
- [ ] Install additional dependencies (@tanstack/react-query, @tanstack/react-query-devtools, biome)

**Validation**: `cd frontend && npm run dev` starts dev server successfully

**Dependencies**: None (can be done in parallel with 1.1)

### 1.3 Initialize backend project
- [ ] Create backend/ directory structure (app/api, app/core, app/schemas, app/services, tests)
- [ ] Create environment.yml with Python 3.11+ and dependencies
- [ ] Create pyproject.toml with FastAPI and testing dependencies
- [ ] Create app/main.py with basic FastAPI app
- [ ] Create health check endpoint in app/api/v1/health.py

**Validation**: `cd backend && conda env create -f environment.yml` succeeds

**Dependencies**: None (can be done in parallel with 1.1, 1.2)

## Phase 2: Frontend Configuration (Depends on 1.2)

### 2.1 Configure Biome
- [ ] Create biome.json in frontend/ with sensible defaults
- [ ] Enable TypeScript and React rules
- [ ] Configure formatter (2 spaces, 100 char line length)
- [ ] Add npm scripts: lint, format, typecheck
- [ ] Run Biome on existing files to format them

**Validation**: `cd frontend && npm run lint` passes, `npm run format` formats files

**Dependencies**: 1.2 (frontend project initialized)

### 2.2 Configure Vite
- [ ] Create vite.config.ts with React plugin
- [ ] Configure dev server port 5173
- [ ] Set up proxy to backend (localhost:8000)
- [ ] Configure build options (outDir, source maps)
- [ ] Add path aliases (@/* for src/*)

**Validation**: Dev server starts on port 5173, proxy works, build succeeds

**Dependencies**: 2.1 (Biome configured)

### 2.3 Create frontend base components and TanStack Query setup
- [ ] Create App.tsx with QueryClientProvider setup
- [ ] Configure QueryClient with sensible defaults (staleTime, cacheTime)
- [ ] Add TanStack Query DevTools for development
- [ ] Create sample component in src/components/
- [ ] Create custom hook example in src/hooks/
- [ ] Create API query functions in src/services/ (using fetch)
- [ ] Create TypeScript types in src/types/
- [ ] Create example useQuery hook for data fetching
- [ ] Create example useMutation hook for mutations

**Validation**: TypeScript compiles without errors, app renders in browser, queries work

**Dependencies**: 2.2 (Vite configured)

### 2.4 Configure frontend testing
- [ ] Install Vitest and testing dependencies
- [ ] Create vitest.config.ts
- [ ] Add test script to package.json
- [ ] Create sample test for a component
- [ ] Verify tests run successfully

**Validation**: `cd frontend && npm run test` runs and passes sample test

**Dependencies**: 2.3 (base components created)

## Phase 3: Backend Configuration (Depends on 1.3)

### 3.1 Create FastAPI application structure
- [ ] Create app/main.py with FastAPI instance
- [ ] Configure CORS for frontend (localhost:5173)
- [ ] Set up API router versioning (app/api/v1/)
- [ ] Create app/core/config.py for configuration
- [ ] Add health check endpoint

**Validation**: Server starts on port 8000, /docs shows OpenAPI docs

**Dependencies**: 1.3 (backend directory structure created)

### 3.2 Create Pydantic schemas
- [ ] Create app/schemas/ directory
- [ ] Create base schema classes
- [ ] Create sample request/response schemas
- [ ] Add schema validation examples
- [ ] Document schema usage

**Validation**: Schemas validate correctly, appear in OpenAPI docs

**Dependencies**: 3.1 (FastAPI app created)

### 3.3 Create service layer
- [ ] Create app/services/ directory
- [ ] Create sample service with business logic
- [ ] Implement async patterns
- [ ] Add error handling
- [ ] Write service tests

**Validation**: Services work correctly, tests pass

**Dependencies**: 3.2 (schemas created)

### 3.4 Configure pytest
- [ ] Create pytest.ini in backend/
- [ ] Install pytest and pytest-asyncio
- [ ] Create conftest.py with test fixtures
- [ ] Create sample API test
- [ ] Configure pytest-cov for coverage
- [ ] Add test script to pyproject.toml

**Validation**: `cd backend && pytest` runs and passes all tests

**Dependencies**: 3.3 (service layer created)

## Phase 4: Makefile Integration (Depends on 2.x, 3.x)

### 4.1 Implement development commands
- [ ] Add `make dev` target (start both frontend and backend)
- [ ] Add `make dev-frontend` target
- [ ] Add `make dev-backend` target
- [ ] Ensure proper process management (use background processes or parallel)
- [ ] Add cleanup on Ctrl+C

**Validation**: `make dev` starts both services, Ctrl+C stops both cleanly

**Dependencies**: 2.2, 3.1 (both dev servers configured)

### 4.2 Implement build commands
- [ ] Add `make build` target (build both)
- [ ] Add `make build-frontend` target
- [ ] Add `make build-backend` target
- [ ] Add `make clean` target
- [ ] Add `make clean-all` target

**Validation**: All build commands create artifacts, clean commands remove them

**Dependencies**: 2.2, 3.1 (build systems configured)

### 4.3 Implement testing commands
- [ ] Add `make test` target (run all tests)
- [ ] Add `make test-frontend` target
- [ ] Add `make test-backend` target
- [ ] Add `make coverage` target
- [ ] Ensure proper exit codes

**Validation**: All test commands run and report correctly

**Dependencies**: 2.4, 3.4 (testing configured)

### 4.4 Implement code quality commands
- [ ] Add `make lint` target (check both)
- [ ] Add `make lint-frontend` target
- [ ] Add `make lint-backend` target
- [ ] Add `make format` target (format both)
- [ ] Add `make typecheck` target (TypeScript only)

**Validation**: All lint/format commands work correctly

**Dependencies**: 2.1, 3.4 (Biome and pytest configured)

### 4.5 Implement setup commands
- [ ] Add `make setup` target
- [ ] Add `make update-deps` target
- [ ] Add prerequisite checks (Node.js, conda, make)
- [ ] Add helpful error messages for missing tools

**Validation**: `make setup` runs successfully on fresh clone

**Dependencies**: 4.1-4.4 (all commands implemented)

## Phase 5: Integration and Documentation (Depends on all phases)

### 5.1 Create integration example with TanStack Query
- [ ] Add sample API endpoint in backend
- [ ] Create query function in src/services/ to fetch data
- [ ] Create frontend component using useQuery hook
- [ ] Implement proper error handling with error boundaries
- [ ] Add loading and error states (TanStack Query provides these)
- [ ] Test end-to-end flow with cache and refetch behavior
- [ ] Verify TanStack Query DevTools show query state

**Validation**: Frontend successfully fetches and displays data from backend with proper loading/error states

**Dependencies**: 2.3, 3.3 (frontend and backend components created)

### 5.2 Write comprehensive documentation
- [ ] Update README.md with setup instructions
- [ ] Document all Make commands
- [ ] Add architecture overview
- [ ] Document development workflow
- [ ] Add troubleshooting section

**Validation**: New developer can follow README to set up and run project

**Dependencies**: 4.5 (setup commands implemented)

### 5.3 Create example API endpoints
- [ ] Create CRUD endpoints for a sample resource
- [ ] Document endpoints in OpenAPI
- [ ] Add request/response examples
- [ ] Create corresponding frontend UI
- [ ] Write integration tests

**Validation**: API is fully functional and documented

**Dependencies**: 5.1 (integration example working)

### 5.4 Final validation
- [ ] Run all tests: `make test`
- [ ] Run all linters: `make lint`
- [ ] Build everything: `make build`
- [ ] Test full development workflow
- [ ] Verify clean setup from scratch
- [ ] Check all documentation is accurate

**Validation**: All commands work, project is fully functional

**Dependencies**: 5.2, 5.3 (documentation and examples complete)

## Parallelization Opportunities

**Can be done in parallel:**
- Tasks 1.1, 1.2, 1.3 (initial structure setup)
- Tasks 2.1, 2.2, 3.1, 3.2 (frontend and backend config)
- Tasks 2.3, 2.4, 3.3, 3.4 (feature development and testing)
- Tasks 4.1, 4.2, 4.3, 4.4 (different Makefile target categories)

**Must be sequential:**
- Phase 1 → Phase 2 (frontend needs base structure)
- Phase 1 → Phase 3 (backend needs base structure)
- Phase 2/3 → Phase 4 (Makefile needs configured services)
- Phase 4 → Phase 5 (integration needs all commands working)
