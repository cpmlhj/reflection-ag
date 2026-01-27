# Spec: Backend Project Structure

## ADDED Requirements

### Requirement: Backend Project Scaffold
The backend MUST be initialized with FastAPI and Python using community best practices.

#### Scenario: Project initialization
**Given** a new project directory
**When** the backend initialization is executed
**Then** the project MUST have:
- FastAPI application with async support
- Python 3.11+ specified in environment.yml
- Proper directory structure (app/api, app/core, app/schemas, app/services)
- Entry point at app/main.py
- Pydantic v2 for data validation
- UVicorn as ASGI server

### Requirement: Conda Environment
The backend MUST use Conda for reproducible Python environment management.

#### Scenario: Environment creation
**Given** the backend project is initialized
**When** a developer runs `conda env create -f environment.yml`
**Then** Conda MUST:
- Create environment named "reflection-agent"
- Install Python 3.11 or higher
- Install all dependencies from environment.yml
- Allow activation via `conda activate reflection-agent`

#### Scenario: Environment reproducibility
**Given** the conda environment exists
**When** environment.yml is updated
**Then** developers MUST be able to:
- Update environment with `conda env update -f environment.yml`
- Export environment with `conda env export`
- Reproduce exact environment across machines

### Requirement: FastAPI Application Structure
The backend MUST follow a modular FastAPI structure with clear separation of concerns.

#### Scenario: Application entry point
**Given** the backend project structure
**When** the application starts
**Then** app/main.py MUST:
- Create FastAPI application instance
- Include API routers with proper versioning
- Configure CORS for frontend communication
- Provide health check endpoint
- Include automatic OpenAPI documentation

#### Scenario: API organization
**Given** the backend structure
**When** API endpoints are created
**Then** the project MUST have:
- app/api/v1/ directory for version 1 endpoints
- Separate router files per domain (e.g., health.py, items.py)
- Pydantic schemas in app/schemas/
- Business logic in app/services/
- Configuration in app/core/

### Requirement: Pydantic Schemas
The backend MUST use Pydantic v2 for request/response validation.

#### Scenario: Request validation
**Given** FastAPI is configured with Pydantic
**When** a request is received
**Then** the application MUST:
- Validate request bodies against schemas
- Return 422 for invalid data with clear error messages
- Support all primitive types and complex objects
- Provide automatic OpenAPI schema generation

#### Scenario: Response validation
**Given** Pydantic schemas are defined
**When** responses are returned
**Then** the application MUST:
- Validate responses against response models
- Include proper type hints for IDE support
- Support enum types and custom validators
- Handle datetime serialization properly

### Requirement: Async Configuration
The backend MUST use async/await patterns for optimal performance.

#### Scenario: Async endpoints
**Given** FastAPI is configured
**When** endpoints are defined
**Then** route handlers MUST:
- Use `async def` for all route handlers
- Use async database operations when databases are added
- Avoid blocking I/O in async contexts
- Use `await` for async operations

#### Scenario: Server configuration
**Given** UVicorn is used as server
**When** the server starts
**Then** UVicorn MUST:
- Use uvloop for optimal performance on Unix
- Support http/2 when available
- Handle graceful shutdown
- Log requests appropriately

### Requirement: Testing Infrastructure
The backend MUST include pytest with async support for testing.

#### Scenario: Test setup
**Given** the backend project is initialized
**When** tests are written
**Then** the project MUST have:
- pytest configured in pyproject.toml
- pytest-asyncio for async test support
- tests/ directory mirroring app/ structure
- Test client from FastAPI TestClient
- At least one sample test demonstrating async testing

#### Scenario: Running tests
**Given** tests are written
**When** a developer runs `pytest`
**Then** pytest MUST:
- Discover and run all tests in tests/
- Support async test functions
- Provide clear failure messages
- Exit with non-zero on test failures
- Support coverage reporting with pytest-cov

### Requirement: Python Dependencies
The backend MUST specify all dependencies using modern Python packaging standards.

#### Scenario: Dependency specification
**Given** the backend project
**When** dependencies are managed
**Then** the project MUST have:
- environment.yml for conda environment
- pyproject.toml for pip-installable packages
- fastapi as web framework
- uvicorn[standard] as ASGI server
- pydantic for data validation
- pytest and pytest-asyncio for testing
- All versions pinned for reproducibility

#### Scenario: Dependency installation
**Given** dependencies are specified
**When** a developer creates the conda environment
**Then** the installation MUST:
- Install exact versions specified in environment.yml
- Resolve dependencies correctly
- Support both conda and pip packages
- Allow development mode installs

## MODIFIED Requirements
None (new project setup)

## REMOVED Requirements
None (new project setup)
