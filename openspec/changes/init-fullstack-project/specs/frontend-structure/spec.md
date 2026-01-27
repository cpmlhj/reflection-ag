# Spec: Frontend Project Structure

## ADDED Requirements

### Requirement: Frontend Project Scaffold
The frontend MUST be initialized with React, TypeScript, and Vite using community best practices.

#### Scenario: Project initialization
**Given** a new project directory
**When** the frontend initialization is executed
**Then** the project MUST have:
- Vite 5+ configured for React + TypeScript
- React 18+ with TypeScript support
- TypeScript 5+ with strict mode enabled
- Proper directory structure (src/components, src/hooks, src/services, src/types)
- Entry point at src/main.tsx and index.html
- Package.json with all necessary dependencies

### Requirement: Biome Configuration
The frontend MUST use Biome for linting and formatting with sensible defaults.

#### Scenario: Code quality enforcement
**Given** the frontend project is initialized
**When** Biome is configured
**Then** the project MUST have:
- biome.json configuration file
- Lint rules enabled for TypeScript and React
- Formatter with consistent indentation (2 spaces)
- Line length limit of 100 characters
- Scripts for lint and format in package.json

#### Scenario: Biome integration
**Given** Biome is configured
**When** a developer runs `npm run lint` or `npm run format`
**Then** Biome MUST:
- Check all TypeScript and TSX files
- Report linting errors with clear messages
- Auto-fix formatting issues where possible
- Exit with non-zero code on errors

### Requirement: TypeScript Configuration
The frontend MUST have TypeScript configured with strict type checking and modern features.

#### Scenario: Type safety
**Given** the frontend project uses TypeScript
**When** tsconfig.json is configured
**Then** the configuration MUST include:
- strict mode enabled
- target ES2020 or higher
- module resolution set to "bundler"
- path aliases (@/* for src/*)
- JSX support for React
- skipLibCheck for faster builds

#### Scenario: Type checking
**Given** TypeScript is configured
**When** a developer writes TypeScript code
**Then** the compiler MUST:
- Catch type errors at build time
- Provide autocomplete in IDEs
- Allow explicit any with @ts-ignore comments
- Support modern TypeScript syntax

### Requirement: Vite Configuration
The frontend MUST use Vite for development server and production builds.

#### Scenario: Development server
**Given** Vite is configured
**When** a developer runs `npm run dev`
**Then** Vite MUST:
- Start development server on port 5173
- Enable hot module replacement
- Proxy backend API requests to port 8000
- Show clear error overlays for issues

#### Scenario: Production build
**Given** Vite is configured
**When** a developer runs `npm run build`
**Then** Vite MUST:
- Create optimized production build in dist/
- Minify JavaScript and CSS
- Generate source maps
- Report bundle size analysis
- Exit with 0 on success

### Requirement: React Application Structure
The frontend MUST follow a clear React component structure with proper separation of concerns.

#### Scenario: Component organization
**Given** the frontend project structure
**When** components are created
**Then** the project MUST have:
- src/components/ for reusable components
- src/App.tsx as root component
- src/main.tsx as entry point
- Functional components with hooks
- Proper TypeScript props typing

#### Scenario: API integration
**Given** the frontend needs to communicate with backend
**When** API calls are made using TanStack Query
**Then** the project MUST have:
- src/services/ directory for API query functions
- QueryClient provider configured in App.tsx
- Type definitions for API responses
- Query hooks for data fetching with proper error handling
- Mutation hooks for write operations

### Requirement: TanStack Query Configuration
The frontend MUST use TanStack Query with proper configuration for optimal developer experience.

#### Scenario: Query client setup
**Given** TanStack Query is installed
**When** the application initializes
**Then** the app MUST have:
- QueryClient configured with sensible defaults
- QueryClientProvider wrapping the application in App.tsx
- Proper error boundary setup for query errors
- Development mode DevTools enabled

#### Scenario: Query usage patterns
**Given** TanStack Query is configured
**When** components need to fetch data
**Then** developers MUST be able to:
- Use useQuery hook for data fetching
- Use useMutation hook for write operations
- Configure caching and refetching strategies
- Handle loading and error states declaratively
- Use infinite queries for pagination (if needed)

#### Scenario: Type safety
**Given** TypeScript is configured
**When** queries are written
**Then** TanStack Query MUST:
- Infer types from query functions
- Provide full TypeScript support for query options
- Type mutation variables and responses
- Support generic type parameters for custom hooks

### Requirement: Development Dependencies
The frontend MUST include all necessary development dependencies for a modern React workflow.

#### Scenario: Dependency installation
**Given** the frontend project is initialized
**When** dependencies are installed via npm
**Then** package.json MUST include:
- react and react-dom as runtime dependencies
- vite as build tool
- typescript and @types/react for TypeScript
- @vitejs/plugin-react for React support
- biome for linting and formatting
- @tanstack/react-query for data fetching and state management
- @tanstack/react-query-devtools for debugging (dev dependency)

## MODIFIED Requirements
None (new project setup)

## REMOVED Requirements
None (new project setup)
