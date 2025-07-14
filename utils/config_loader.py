import yaml
from pathlib import Path

def load_config(path=None):
    if path is None:
        # Dynamically locate the config.yaml relative to this file
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir / "config" / "config.yaml"

    with open(path, 'r') as file:
        return yaml.safe_load(file)
