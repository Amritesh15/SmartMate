# SmartMate

Small personal assistant project that integrates with Google Calendar and a GPT node. Contains example nodes and helper scripts.

Quick start

1. Create a Python virtual environment and install dependencies:

```powershell
python -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; pip install -r requirements.txt
```

2. Obtain Google API credentials and place them in `credentials.json`.

3. Run app:

```powershell
python app.py
```

Files of note:
- `app.py` - main entrypoint
- `nodes/calendar_node.py` - calendar integration node
- `nodes/gpt_node.py` - GPT integration node
