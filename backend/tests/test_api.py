"""API endpoint tests"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_endpoint(async_client: AsyncClient):
    """Test root endpoint"""
    response = await async_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Reflection Agent API"


@pytest.mark.asyncio
async def test_health_endpoint(async_client: AsyncClient):
    """Test health check endpoint"""
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "message" in data


@pytest.mark.asyncio
async def test_docs_endpoint(async_client: AsyncClient):
    """Test that OpenAPI docs are accessible"""
    response = await async_client.get("/docs")
    assert response.status_code == 200
