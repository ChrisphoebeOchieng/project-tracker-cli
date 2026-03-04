import json
import os
from typing import List, Dict, Any

DATA_FILE = "data/project_data.json"

def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")

def load_data() -> Dict[str, Any]:
    ensure_data_dir()
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": [], "projects": [], "tasks": []}
    except json.JSONDecodeError:
        print("Warning: Data file corrupted. Initializing new data.")
        return {"users": [], "projects": [], "tasks": []}

def save_data(data: Dict[str, Any]):
    ensure_data_dir()
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")
        raise