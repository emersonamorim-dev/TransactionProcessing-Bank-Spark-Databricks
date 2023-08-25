import json
from typing import Any

def load_config(path: str) -> dict:
    """Load a JSON configuration file."""
    with open(path, 'r') as file:
        return json.load(file)

def save_config(config: dict, path: str) -> None:
    """Save a configuration dictionary to a JSON file."""
    with open(path, 'w') as file:
        json.dump(config, file, indent=4)

def update_config(path: str, new_config: dict) -> None:
    """Update values in an existing configuration file."""
    config = load_config(path)
    config.update(new_config)
    save_config(config, path)

def get_config_value(path: str, key: str) -> Any:
    """Get a specific value from a configuration file using a key."""
    config = load_config(path)
    return config.get(key)

def set_config_value(path: str, key: str, value: Any) -> None:
    """Set a specific value in a configuration file using a key."""
    config = load_config(path)
    config[key] = value
    save_config(config, path)

