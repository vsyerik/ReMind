"""
Configuration management for ReMind Pulse.

This module provides functions for loading and accessing configuration
from various sources, including config files and environment variables.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional

# Default configuration
DEFAULT_CONFIG = {
    "custom_stopwords": [],
    "journal_dir": "/Users/yourname/Journal",  # <-- generic placeholder
    "days_back": 7
}


def get_config_paths() -> list:
    """
    Get a list of possible configuration file paths in order of precedence.
    
    Returns:
        List of Path objects representing possible config file locations
    """
    return [
        Path("config.yaml"),  # Current directory
        Path.home() / ".config" / "remind" / "config.yaml",  # User config directory
        Path(__file__).parent / "config.yaml",  # Package directory
    ]


def load_config() -> Dict[str, Any]:
    """
    Load configuration from the first available config file.
    
    Returns:
        Dictionary containing configuration values
    """
    for config_path in get_config_paths():
        if config_path.exists():
            try:
                with open(config_path, "r") as f:
                    config = yaml.safe_load(f)
                    if config is None:
                        config = {}
                    return {**DEFAULT_CONFIG, **config}
            except Exception as e:
                print(f"Error loading config from {config_path}: {e}")
    
    return DEFAULT_CONFIG


def get_env_config() -> Dict[str, Any]:
    """
    Get configuration from environment variables.
    
    Environment variables should be prefixed with REMIND_
    For example, REMIND_JOURNAL_DIR will override journal_dir
    
    Returns:
        Dictionary containing configuration from environment variables
    """
    env_config = {}
    prefix = "REMIND_"
    
    for key, value in os.environ.items():
        if key.startswith(prefix):
            config_key = key[len(prefix):].lower()
            env_config[config_key] = value
    
    return env_config


def get_config() -> Dict[str, Any]:
    """
    Get the complete configuration, combining defaults, config files,
    and environment variables in order of precedence.
    
    Returns:
        Dictionary containing the complete configuration
    """
    config = load_config()
    env_config = get_env_config()
    
    # Override with environment variables
    for key, value in env_config.items():
        config[key] = value
    
    return config


# Singleton config instance
_config = None


def config() -> Dict[str, Any]:
    """
    Get the configuration singleton.
    
    Returns:
        Dictionary containing the complete configuration
    """
    global _config
    if _config is None:
        _config = get_config()
    return _config


def get(key: str, default: Any = None) -> Any:
    """
    Get a configuration value by key.
    
    Args:
        key: The configuration key
        default: Default value if key is not found
        
    Returns:
        The configuration value or default
    """
    return config().get(key, default)