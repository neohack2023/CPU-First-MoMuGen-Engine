"""Tests for the project state schema structure in v0.1."""

from engine.state import PROJECT_STATE_SCHEMA, default_project_state


def test_schema_has_required_sections() -> None:
    """Verify top-level required keys are declared."""

    required = set(PROJECT_STATE_SCHEMA.get("required", []))
    assert {"project", "timebase", "layers", "determinism"}.issubset(required)


def test_default_state_matches_schema_keys() -> None:
    """Ensure the default state includes all required sections."""

    state = default_project_state()
    for key in PROJECT_STATE_SCHEMA["required"]:
        assert key in state
