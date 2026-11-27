"""Capture the simulation environment for a run record (RFC-0008 reproducibility).

Every run should record which simulator produced it, so a result can be traced
back to an exact, reinstallable environment. ``capture_run_env`` snapshots the
``viva-genesis-sim`` version (+ the rest of the framework/engine package env, the
workspace commit, python and platform) and the derived ``env_id`` hash, ready to
merge into a study's run entry.

It degrades gracefully: if ``viva-discovery-engine`` (which provides the canonical
capture) is not installed, it returns ``{}`` so a run still records — it just
omits the env snapshot rather than failing.
"""
from __future__ import annotations

from typing import Any


def capture_run_env(ws_root: Any = None) -> dict:
    """Return ``{"env": <env dict>, "env_id": <hash>}`` for a run record.

    ``env`` includes ``sim_packages`` (with ``viva-genesis-sim``'s version/git_sha),
    ``workspace_commit``, ``python`` and ``platform``. Returns ``{}`` if the
    capture dependency is unavailable or capture fails.
    """
    try:
        from discovery_engine.study.run_registry import capture_environment, env_id
    except Exception:
        return {}
    try:
        from ._paths import workspace_root
        env = capture_environment(ws_root or workspace_root(), pkg="viva-genesis-sim")
        return {"env": env, "env_id": env_id(env)}
    except Exception:
        return {}
