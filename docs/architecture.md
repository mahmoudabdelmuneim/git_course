# Architecture

## Planned processing pipeline

```text
Camera Frames
    ?
Pose Estimation
    ?
Landmark Processing
    ?
Exercise Engine
    ?
Repetition Counting
    ?
Form Analysis
    ?
Feedback Engine
    ?
Workout Results
```

This describes intended future processing only. The current implementation provides an HTTP health endpoint and initial Pydantic contracts; it does not process frames or generate AI results.

## Boundaries

- `app/api`: HTTP routes and dependency wiring.
- `app/core`: settings, logging, and shared application setup.
- `app/schemas`: versionable interfaces between API and future processing components.
- `app/ai/pose`: pose estimation, landmark extraction/normalization, confidence.
- `app/ai/exercises`: exercise state machines and repetition rules.
- `app/ai/form_analysis`: alignment and movement quality evaluation.
- `app/ai/feedback`: prioritization and formatting of analysis feedback.

The schemas are initial contracts subject to team review, not a final public API commitment. Keep future inference modules independent of FastAPI and communicate through explicit schemas.
