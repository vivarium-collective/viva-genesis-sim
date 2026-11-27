"""capture_run_env records the simulator for run-level reproducibility."""
import pytest


def test_capture_run_env_never_raises():
    from viva_genesis.run_env import capture_run_env
    capture_run_env()  # must not raise even if the capture dep is missing


def test_capture_run_env_records_viva_genesis_sim():
    from viva_genesis.run_env import capture_run_env
    rec = capture_run_env()
    if not rec:
        pytest.skip("viva-discovery-engine not installed (capture unavailable)")
    assert isinstance(rec.get("env_id"), str) and rec["env_id"]
    sim = rec["env"]["sim_packages"]
    assert "viva-genesis-sim" in sim
    assert sim["viva-genesis-sim"].get("version")
