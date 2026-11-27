"""Load network models from committed model files (model-as-data).

Instead of a hardcoded model string inside each network Process, models live as
committed data — antimony (``.ant``) or SBML (``.xml``) files under
``viva_genesis/data/models/`` — and are integrated by the imported
``viva_tellurium`` / libRoadRunner engine. One loader, reused by every network
process, so adding a model is adding a file, not a module.
"""
from __future__ import annotations

from pathlib import Path

MODELS_DIR = Path(__file__).resolve().parent / "data" / "models"


def read_model(model: str) -> tuple[str, str]:
    """Return ``(model_text, format)`` for ``model`` — a ``data/models/`` filename, an
    absolute path, or inline antimony/SBML text. Format is ``"sbml"`` for ``.xml``/
    ``.sbml`` (or text starting with ``<?xml``), else ``"antimony"``."""
    s = str(model)
    if "\n" in s or s.lstrip().startswith("<?xml"):
        return s, ("sbml" if s.lstrip().startswith("<?xml") else "antimony")
    p = Path(s)
    if not p.is_absolute():
        p = MODELS_DIR / s
    return p.read_text(), ("sbml" if p.suffix.lower() in (".xml", ".sbml") else "antimony")


def load_roadrunner(model: str):
    """Load a libRoadRunner instance for ``model`` via the imported viva_tellurium
    engine (the genuine SBML/antimony integrator)."""
    from viva_tellurium import load_roadrunner  # public engine API
    text, fmt = read_model(model)
    return load_roadrunner(text, model_format=fmt)
