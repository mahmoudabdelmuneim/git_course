"""Shared API schemas."""

from typing import Literal

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Health endpoint response."""

    status: Literal["healthy"]
    app_name: str
    version: str


class APIModel(BaseModel):
    """Base schema with strict handling of unexpected input fields."""

    model_config = ConfigDict(extra="forbid")
