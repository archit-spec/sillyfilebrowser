from flask import Flask
from flask import jsonify
from dataclasses import dataclass

@dataclass
class Settings:
    """dataclass for storing configuration settings."""
    model: str  # Name of the huggingface model identifier (e.g., "Salesforce/blip-image-captioning-base")
    is_cuda: bool = False  # Default to using CPU, set to True for GPU if available
    indexer: str = None  # Placeholder for the indexer object



