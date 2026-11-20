"""Initial data contracts for future workout processing."""

from datetime import datetime
from enum import StrEnum
from typing import Any
from uuid import UUID

from pydantic import Field, NonNegativeInt, confloat

from app.schemas.common import APIModel


class FeedbackCategory(StrEnum):
    FORM = "form"
    MOTIVATION = "motivation"
    SAFETY = "safety"
    GENERAL = "general"


class FeedbackSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class Landmark(APIModel):
    name: str | None = None
    index: NonNegativeInt | None = None
    x: float
    y: float
    z: float
    visibility: confloat(ge=0, le=1) | None = None
    presence: confloat(ge=0, le=1) | None = None


class PoseResult(APIModel):
    landmarks: list[Landmark] = Field(default_factory=list)
    detection_confidence: confloat(ge=0, le=1) | None = None
    timestamp: datetime
    processing_metadata: dict[str, Any] = Field(default_factory=dict)


class WorkoutSession(APIModel):
    session_id: UUID
    user_id: UUID | None = None
    exercise_type: str
    start_timestamp: datetime
    end_timestamp: datetime | None = None
    duration_seconds: float | None = Field(default=None, ge=0)
    total_repetitions: NonNegativeInt = 0
    valid_repetitions: NonNegativeInt = 0
    invalid_repetitions: NonNegativeInt = 0


class ExerciseFeedback(APIModel):
    category: FeedbackCategory
    message: str = Field(min_length=1)
    severity: FeedbackSeverity
    timestamp: datetime
