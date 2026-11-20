# Team workflow

## Ownership

- AI Engineer 1: pose estimation and landmark processing (`app/ai/pose`).
- AI Engineer 2: exercise state and repetition logic (`app/ai/exercises`).
- AI Engineer 3: form analysis (`app/ai/form_analysis`).
- AI Engineer 4: evaluation data, feedback, and shared schema coordination (`app/ai/feedback`, `data/`).
- Mobile developer: mobile integration coordination through the API contracts; mobile code stays in its own repository.

Agree on final ownership as a team. Schemas and shared core are collaborative areas; discuss changes before modifying contracts used by another module.

## Branches and reviews

Keep `main` releasable and integrate through `develop`. Create focused branches from `develop`, for example `feature/pose-estimation`, `feature/exercise-engine`, `feature/form-analysis`, `feature/data-evaluation`, and `feature/mobile-integration`. Use `fix/` for defects and short kebab-case descriptions.

Open a pull request to `develop` with context, scope, and verification steps. Require at least one teammate review, passing tests and Ruff checks, and updated docs/contracts where relevant. Resolve review comments and avoid merging your own unreviewed changes. Communicate before changing another owner's module or shared interface. Keep PRs focused; never commit secrets, datasets, videos, or model weights.

Commit messages should use a simple Conventional Commits style, such as `feat(pose): define landmark interface` or `docs: clarify local setup`.
