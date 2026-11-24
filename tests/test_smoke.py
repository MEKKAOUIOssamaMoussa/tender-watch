import os
"""Smoke test proving the package is importable and the test pipeline runs."""

import tender_watch


def test_package_is_importable() -> None:
    """Verify tender_watch can be imported; tests no business logic yet."""
    assert tender_watch.__doc__ is not None
