"""Performance and quality metric placeholders for v0.1.

The engine will eventually emit telemetry such as RTF and peak memory; for now
this module provides structured containers for those values.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class MetricsSnapshot:
    """Immutable snapshot of runtime metrics."""

    rtf: Optional[float]
    peak_memory_mb: Optional[float]


def build_snapshot(rtf: Optional[float] = None, peak_memory_mb: Optional[float] = None) -> MetricsSnapshot:
    """Create a metrics snapshot with optional values."""

    return MetricsSnapshot(rtf=rtf, peak_memory_mb=peak_memory_mb)
