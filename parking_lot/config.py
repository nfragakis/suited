import os

SPECIFICATION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs")
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
