# Pose module

**Responsibility:** Pose estimation, landmark extraction and normalization, and pose confidence.

**Input contract:** Camera frames (contract to be agreed); future image/frame representation.

**Output contract:** `PoseResult` with `Landmark` entries from `app.schemas.workout`.

**Owner:** AI Engineer 1 (proposed; team confirmation pending).

**Status:** Boundary only; no pose implementation.

**Future tasks:** Select and evaluate pose approach; define frame and coordinate conventions; implement extraction and confidence; add tests and evaluation fixtures.
