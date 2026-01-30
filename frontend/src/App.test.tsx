import { describe, it, expect, vi } from "vitest"
import { render, screen } from "@testing-library/react"
import App from "./App"

// Mock the HealthStatus component to avoid API calls during tests
vi.mock("@/components/HealthStatus", () => ({
  HealthStatus: () => <div data-testid="health-status">Mocked Health Status</div>,
}))

describe("App", () => {
  it("renders the app title", () => {
    render(<App />)
    expect(screen.getByText("Reflection Agent")).toBeInTheDocument()
  })

  it("renders the subtitle", () => {
    render(<App />)
    expect(screen.getByText("Full-stack application with React + FastAPI")).toBeInTheDocument()
  })

  it("renders the HealthStatus component", () => {
    render(<App />)
    expect(screen.getByTestId("health-status")).toBeInTheDocument()
  })
})
