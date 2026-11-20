# Development setup

Use Python 3.11. Create and activate a virtual environment from the repository root.

## Windows PowerShell

```powershell
python -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
Copy-Item .env.example .env
```

If PowerShell blocks activation, use `.venv\Scripts\activate.bat` in Command Prompt. The `python -3.11` launcher requires Python 3.11 installed and registered with the Windows Python launcher.

## Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
cp .env.example .env
```

Both platforms use the same pip requirements; the selected package versions publish compatible wheels for supported Python versions. OpenCV is included for future frame handling, but no model or dataset is downloaded.

## Run locally

```bash
uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`; Swagger: `http://127.0.0.1:8000/docs` in development.

## Checks

```bash
pytest
pytest --cov=app --cov-report=term-missing
ruff check .
ruff format --check .
```
