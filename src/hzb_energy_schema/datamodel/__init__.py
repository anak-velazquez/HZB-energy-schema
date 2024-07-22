from pathlib import Path
from .hzb_energy_schema import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "hzb_energy_schema.yaml"
