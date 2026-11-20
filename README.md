# AI Home Workout

An AI powered home workout challenge platform, developed by four AI engineers alongside a mobile application developer. The platform is intended to use camera based movement analysis to count repetitions, assess form, give timely feedback, and support challenges.

## Problem and solution

People exercising at home often lack immediate coaching and consistent progress tracking. This project plans a modular computer vision pipeline that can interpret movement and provide workout guidance. This repository is currently the software foundation only; it does not yet detect poses, count repetitions, assess form, train models, or provide challenge features.

## Planned features

- Pose and landmark processing from camera frames.
- Exercise-specific repetition counting.
- Form analysis and prioritized feedback.
- Workout session results and challenge integration.

## Technology

Python 3.11, FastAPI, Pydantic v2, NumPy, OpenCV, MediaPipe, Pytest, Ruff, and Git. Runtime dependencies are pinned in `requirements.txt`; developer tools are in `requirements-dev.txt`.

## Architecture and structure

See [architecture](docs/architecture.md) for the planned pipeline and module contracts.

```text
app/                 API, core settings, schemas, AI module boundaries, tests
configs/             Configuration notes
data/                Reserved data locations (do not commit recordings)
docs/                Architecture, setup, and team workflow
notebooks/           Exploration only
scripts/             Repeatable helper scripts
```

## Setup

Python 3.11 is required. Follow [development setup](docs/development_setup.md) for Windows PowerShell and Linux venv instructions. Copy `.env.example` to `.env` for local settings; `.env` is ignored by Git.

## Run

```bash
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`; Swagger is at `http://127.0.0.1:8000/docs` in development. The implemented route is `GET /api/v1/health`.

## Test and code quality

```bash
pytest
pytest --cov=app --cov-report=term-missing
ruff check .
ruff format --check .
ruff format .
```

## Team

Four AI engineers own pose, exercise logic, form analysis, and evaluation/feedback. The mobile developer coordinates API integration while mobile code remains separate. See [team workflow](docs/team_workflow.md) for branch and review practices.

## Status and roadmap

Implemented: configurable FastAPI shell, health check, logging, CORS preparation, initial workout schemas, test and lint configuration. Planned: team review of schemas; agree on camera-frame contract; build and evaluate pose module; then exercise logic, form analysis, and feedback; coordinate API integration with mobile.
