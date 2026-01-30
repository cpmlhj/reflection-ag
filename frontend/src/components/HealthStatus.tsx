import { useHealth } from "@/hooks/useHealth"

export function HealthStatus() {
  const { data, isLoading, error, isError } = useHealth()

  if (isLoading) {
    return (
      <div className="p-5 bg-gray-100 rounded-lg">
        <p>Loading health status...</p>
      </div>
    )
  }

  if (isError) {
    return (
      <div className="p-5 bg-red-50 rounded-lg border border-red-500">
        <p className="text-red-800">
          Error: {error instanceof Error ? error.message : "Failed to fetch health status"}
        </p>
      </div>
    )
  }

  return (
    <div className="p-5 bg-green-50 rounded-lg border border-green-500">
      <h2 className="mb-2.5 text-green-800">Backend Status</h2>
      <p className="mb-0">
        <strong>Status:</strong> {data?.status}
      </p>
      <p className="mt-0">
        <strong>Message:</strong> {data?.message}
      </p>
    </div>
  )
}
