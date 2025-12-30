"""Tests for determinism guard wiring in v0.1."""

from engine.determinism import guards


def test_execution_guard_exists() -> None:
    """Ensure the execution guard function is exposed."""

    assert callable(guards.set_execution_guards)


def test_execution_guard_docstring_mentions_determinism() -> None:
    """Ensure the guard module documents deterministic intent."""

    assert "deterministic" in (guards.__doc__ or "").lower()
