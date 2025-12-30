"""Timebase helpers for aligning musical grids and codec frames.

The v0.1 spec defines a shared PPQ grid and bar alignment used by all engine
components.
"""

from .timebase import TimebaseConfig, align_frames_to_bar

__all__ = ["TimebaseConfig", "align_frames_to_bar"]
