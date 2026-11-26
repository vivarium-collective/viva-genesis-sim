"""Runtime resolution of the *investigation workspace* root.

The simulator package (``viva_genesis``) no longer lives inside the investigation
repo — it is installed as a dependency (``viva-genesis-sim``). So modules that read
the investigation's committed artifacts (uq posteriors, some study-specific viz)
must resolve the workspace at RUNTIME from the current working directory, not from
``__file__`` (which now points into the installed package, not the workspace).

``workspace_root()`` walks up from the cwd to the nearest directory containing a
``workspace.yaml``. This matches how the investigation is actually run (dashboard,
tests, and CLI all execute from the workspace root). If none is found it returns the
cwd, so callers still produce a sensible (if missing-file) path.
"""
from __future__ import annotations

import os
from pathlib import Path


def workspace_root() -> Path:
    start = Path(os.getcwd()).resolve()
    for d in (start, *start.parents):
        if (d / "workspace.yaml").exists():
            return d
    return start
