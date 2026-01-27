import { useHealth } from '@/hooks/useHealth'

export function HealthStatus() {
  const { data, isLoading, error, isError } = useHealth()

  if (isLoading) {
    return (
      <div style={{ padding: '20px', background: '#f0f0f0', borderRadius: '8px' }}>
        <p>Loading health status...</p>
      </div>
    )
  }

  if (isError) {
    return (
      <div
        style={{
          padding: '20px',
          background: '#ffebee',
          borderRadius: '8px',
          border: '1px solid #ef5350',
        }}
      >
        <p style={{ color: '#c62828' }}>
          Error:{' '}
          {error instanceof Error ? error.message : 'Failed to fetch health status'}
        </p>
      </div>
    )
  }

  return (
    <div
      style={{
        padding: '20px',
        background: '#e8f5e9',
        borderRadius: '8px',
        border: '1px solid #66bb6a',
      }}
    >
      <h2 style={{ margin: '0 0 10px 0', color: '#2e7d32' }}>
        Backend Status
      </h2>
      <p style={{ margin: 0 }}>
        <strong>Status:</strong> {data?.status}
      </p>
      <p style={{ margin: '5px 0 0 0' }}>
        <strong>Message:</strong> {data?.message}
      </p>
    </div>
  )
}
