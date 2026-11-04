"""Ensure the repo root is importable so `import studyengine` works under pytest."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
