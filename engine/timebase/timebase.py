"""Timebase configuration and alignment utilities for v0.1.

This module codifies the default PPQ grid and provides helpers to align codec
frames to bar boundaries as described in the architecture specification.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TimebaseConfig:
    """Defines the musical grid for the engine's timing system."""

    ppq: int = 96
    beats_per_bar: int = 4
    bpm: float = 120.0
    codec_frame_hz: float = 50.0

    @property
    def seconds_per_beat(self) -> float:
        """Return seconds per beat based on BPM."""

        return 60.0 / self.bpm

    @property
    def seconds_per_bar(self) -> float:
        """Return seconds per bar based on beats per bar."""

        return self.seconds_per_beat * self.beats_per_bar


def align_frames_to_bar(frame_index: int, config: TimebaseConfig) -> Tuple[int, int]:
    """Snap a codec frame index to the nearest bar boundary.

    Returns a tuple of (aligned_frame_index, offset_frames).
    """

    frames_per_bar = int(round(config.seconds_per_bar * config.codec_frame_hz))
    if frames_per_bar <= 0:
        raise ValueError("frames_per_bar must be positive")
    aligned = int(round(frame_index / frames_per_bar)) * frames_per_bar
    offset = frame_index - aligned
    return aligned, offset
