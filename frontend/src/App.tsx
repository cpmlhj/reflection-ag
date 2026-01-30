import { HealthStatus } from "@/components/HealthStatus"

function App() {
  return (
    <div className="max-w-2xl mx-auto p-5">
      <h1>Reflection Agent</h1>
      <p>Full-stack application with React + FastAPI</p>
      <div className="mt-8">
        <HealthStatus />
      </div>
    </div>
  )
}

export default App
