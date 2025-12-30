"""JSON schema definition for engine project state in v0.1.

This module defines the canonical structure for project metadata and layer
configuration without implementing persistence.
"""

from __future__ import annotations

from typing import Dict, List

PROJECT_STATE_SCHEMA: Dict[str, object] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "CPU-First MoMuGen Project State",
    "type": "object",
    "required": ["project", "timebase", "layers", "determinism"],
    "properties": {
        "project": {
            "type": "object",
            "required": ["name", "version"],
            "properties": {
                "name": {"type": "string"},
                "version": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"},
            },
            "additionalProperties": False,
        },
        "timebase": {
            "type": "object",
            "required": ["ppq", "bpm", "beats_per_bar"],
            "properties": {
                "ppq": {"type": "integer", "minimum": 1},
                "bpm": {"type": "number", "minimum": 1},
                "beats_per_bar": {"type": "integer", "minimum": 1},
            },
            "additionalProperties": False,
        },
        "layers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "instrument", "model_ref", "token_path"],
                "properties": {
                    "name": {"type": "string"},
                    "instrument": {"type": "string"},
                    "model_ref": {"type": "string"},
                    "token_path": {"type": "string"},
                    "metadata": {"type": "object"},
                },
                "additionalProperties": False,
            },
        },
        "determinism": {
            "type": "object",
            "required": ["seed", "tier"],
            "properties": {
                "seed": {"type": "integer"},
                "tier": {"type": "string", "enum": ["tier1", "tier2", "tier3"]},
                "execution_guard": {"type": "string"},
            },
            "additionalProperties": False,
        },
    },
    "additionalProperties": False,
}


def default_project_state() -> Dict[str, object]:
    """Return a minimal v0.1 project state dictionary."""

    return {
        "project": {
            "name": "Untitled Project",
            "version": "0.1",
            "created_at": "1970-01-01T00:00:00Z",
        },
        "timebase": {
            "ppq": 96,
            "bpm": 120.0,
            "beats_per_bar": 4,
        },
        "layers": [],
        "determinism": {
            "seed": 0,
            "tier": "tier1",
            "execution_guard": "set_execution_guards",
        },
    }
