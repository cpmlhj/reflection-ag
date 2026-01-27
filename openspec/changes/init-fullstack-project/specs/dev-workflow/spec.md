# Spec: Development Workflow

## ADDED Requirements

### Requirement: Makefile Unified Interface
The project MUST provide a Makefile with unified commands for all development operations.

#### Scenario: Command discovery
**Given** a developer clones the repository
**When** they run `make help` or view the Makefile
**Then** they MUST see:
- List of all available commands
- Clear descriptions of what each command does
- Commands organized by category (dev, build, test, lint)

#### Scenario: Development startup
**Given** a developer wants to start development
**When** they run `make dev`
**Then** the command MUST:
- Start both frontend and backend concurrently
- Show clear output from both processes
- Allow stopping with Ctrl+C
- Exit with proper cleanup

#### Scenario: Individual service startup
**Given** a developer wants to work on only one service
**When** they run `make dev-frontend` or `make dev-backend`
**Then** the command MUST:
- Start only the specified service
- Use appropriate development server (Vite or UVicorn)
- Enable hot reload and watch mode
- Show clear startup messages

### Requirement: Build Commands
The project MUST provide commands for creating production builds.

#### Scenario: Production build
**Given** a developer wants to create production builds
**When** they run `make build`
**Then** the command MUST:
- Build both frontend and backend
- Create optimized artifacts
- Report build success or failure
- Show build output locations

#### Scenario: Individual service builds
**Given** a developer wants to build only one service
**When** they run `make build-frontend` or `make build-backend`
**Then** the command MUST:
- Build only the specified service
- Use appropriate build tool (Vite or Python packaging)
- Create production-ready output
- Report build duration and size

### Requirement: Code Quality Commands
The project MUST provide commands for maintaining code quality.

#### Scenario: Linting all code
**Given** a developer wants to check code quality
**When** they run `make lint`
**Then** the command MUST:
- Run Biome on frontend code
- Run appropriate linters on backend code
- Report all issues with clear locations
- Exit with non-zero on errors

#### Scenario: Formatting code
**Given** a developer wants to format code automatically
**When** they run `make format`
**Then** the command MUST:
- Run Biome format on frontend code
- Run appropriate formatters on backend code
- Format files in place
- Report number of files formatted

#### Scenario: Type checking
**Given** the frontend uses TypeScript
**When** a developer runs `make typecheck`
**Then** the command MUST:
- Run TypeScript compiler in check mode
- Report type errors with file locations
- Exit with non-zero on type errors
- Support watch mode for development

### Requirement: Testing Commands
The project MUST provide commands for running tests.

#### Scenario: Running all tests
**Given** a developer wants to run all tests
**When** they run `make test`
**Then** the command MUST:
- Run frontend tests (if configured)
- Run backend tests with pytest
- Show clear test results
- Report coverage if available
- Exit with non-zero on failures

#### Scenario: Running individual test suites
**Given** a developer wants to test only one service
**When** they run `make test-frontend` or `make test-backend`
**Then** the command MUST:
- Run only the specified test suite
- Use appropriate test runner (Vitest or pytest)
- Show test progress and results
- Support watch mode for development

#### Scenario: Coverage reporting
**Given** a developer wants to check test coverage
**When** they run `make coverage`
**Then** the command MUST:
- Run tests with coverage collection
- Generate coverage reports (HTML and terminal)
- Show coverage percentage by file
- Highlight uncovered lines

### Requirement: Environment Setup Commands
The project MUST provide commands for initial project setup.

#### Scenario: First-time setup
**Given** a developer clones the repository for the first time
**When** they run `make setup`
**Then** the command MUST:
- Check for required tools (Node.js, conda, make)
- Create conda environment from environment.yml
- Install frontend dependencies with npm
- Create necessary configuration files
- Report setup success or missing requirements

#### Scenario: Dependency updates
**Given** a developer wants to update dependencies
**When** they run `make update-deps`
**Then** the command MUST:
- Update conda environment
- Update npm packages
- Report any conflicts or issues
- Suggest next steps if updates break things

### Requirement: Documentation Commands
The project MUST provide commands for accessing documentation.

#### Scenario: API documentation
**Given** a developer wants to view API docs
**When** they run `make docs` or `make dev-backend`
**Then** they MUST be able to:
- Access automatic OpenAPI docs at /docs
- View interactive API explorer
- See request/response schemas
- Test API endpoints directly

#### Scenario: Local documentation
**Given** the project has documentation
**When** a developer runs `make docs-serve`
**Then** the command MUST:
- Serve local documentation if available
- Open browser to documentation
- Support hot reload for doc changes

### Requirement: Clean Commands
The project MUST provide commands for cleaning build artifacts.

#### Scenario: Cleaning build artifacts
**Given** a developer wants to remove build artifacts
**When** they run `make clean`
**Then** the command MUST:
- Remove frontend dist/ directory
- Remove Python __pycache__ and .pyc files
- Remove coverage reports
- Remove any temporary files
- Report what was cleaned

#### Scenario: Deep clean
**Given** a developer wants to reset the project
**When** they run `make clean-all`
**Then** the command MUST:
- Run `make clean`
- Remove node_modules/
- Remove .conda environment (with confirmation)
- Remove all installed dependencies
- Warn about destructive nature

## MODIFIED Requirements
None (new project setup)

## REMOVED Requirements
None (new project setup)
