"""Pydantic schemas for health endpoints"""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    message: str


class MessageResponse(BaseModel):
    """Generic message response"""
    message: str
