import json
from pathlib import Path


def load_config(path: str = None):
    base = Path(__file__).resolve().parent.parent
    cfg_path = Path(path) if path else base / "config" / "config.json"
    if not cfg_path.exists():
        cfg_path = Path(__file__).resolve().parent / "config.json"
    with open(cfg_path, encoding="utf-8") as f:
        return json.load(f)
