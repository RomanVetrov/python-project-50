import json
import os

import yaml


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    with open(filepath, "r") as f:
        if ext == ".json":
            return json.load(f)
        if ext in (".yaml", ".yml"):
            return yaml.safe_load(f)
        raise ValueError(f"Unsupported file extension: {ext}")