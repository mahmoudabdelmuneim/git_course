"""Schema validation tests."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from app.schemas.workout import (
    ExerciseFeedback, FeedbackCategory, FeedbackSeverity, Landmark, PoseResult,
)


def test_landmark_accepts_normalized_confidences():
    landmark = Landmark(name="nose", x=0.5, y=0.2, z=0, visibility=0.9, presence=1)
    assert landmark.name == "nose"


def test_landmark_rejects_confidence_outside_range():
    with pytest.raises(ValidationError):
        Landmark(index=0, x=0, y=0, z=0, visibility=1.1)


def test_pose_result_and_feedback_contracts():
    now = datetime.now(UTC)
    pose = PoseResult(landmarks=[], timestamp=now, detection_confidence=0.8)
    feedback = ExerciseFeedback(
        category=FeedbackCategory.FORM, message="Keep your back straight",
        severity=FeedbackSeverity.INFO, timestamp=now,
    )
    assert pose.detection_confidence == 0.8
    assert feedback.severity is FeedbackSeverity.INFO
