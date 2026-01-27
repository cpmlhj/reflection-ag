"""Health check service"""

import asyncpg
from typing import Optional


class HealthService:
    """Service for health check operations"""

    def __init__(self):
        self.db_pool: Optional[asyncpg.Pool] = None

    async def check_database_health(self) -> bool:
        """Check if database connection is healthy"""
        # Placeholder for future database health check
        # When database is added, implement actual connection check
        return True

    async def get_health_status(self) -> dict:
        """Get overall health status"""
        is_healthy = await self.check_database_health()

        return {
            "status": "healthy" if is_healthy else "unhealthy",
            "message": "Reflection Agent API is running"
        }


# Global health service instance
health_service = HealthService()
