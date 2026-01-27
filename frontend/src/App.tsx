import { HealthStatus } from '@/components/HealthStatus'
import './App.css'

function App() {
  return (
    <>
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <h1>Reflection Agent</h1>
        <p>Full-stack application with React + FastAPI</p>
        <div style={{ marginTop: '30px' }}>
          <HealthStatus />
        </div>
      </div>
    </>
  )
}

export default App
