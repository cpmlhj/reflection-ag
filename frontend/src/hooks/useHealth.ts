import { useQuery } from "@tanstack/react-query"
import { fetchHealth } from "@/services/api"

export function useHealth() {
  return useQuery({
    queryKey: ["health"],
    queryFn: fetchHealth,
    staleTime: 1000 * 5, // 5 seconds
    refetchInterval: 1000 * 10, // Refetch every 10 seconds
  })
}
