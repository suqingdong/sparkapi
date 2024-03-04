import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('version.json').open())
MODELS = json.loads(BASE_DIR.joinpath('config', 'models.json').open().read())

__version__ = version_info['version']
