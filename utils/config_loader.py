import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CONFIG_DIR = Path("configs")

def load_yaml(file_name: str):
    path = CONFIG_DIR / file_name
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_env(key: str, default=None):
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Environment variable '{key}' not set")
    return value

def load_settings():
    return load_yaml("settings.yaml")

def load_prompts():
    return load_yaml("prompts.yaml")