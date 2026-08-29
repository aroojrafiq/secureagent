from pathlib import Path

import pytest

from .vulnerable_app import build_export_path


def test_build_export_path_for_normal_filename():
    """Functional test: normal filenames should still be joined to the export directory."""
    assert build_export_path("report.txt") == Path("synthetic-exports") / "report.txt"


def test_build_export_path_rejects_path_traversal_attempt():
    """Security test: traversal attempts should be rejected with ValueError."""
    with pytest.raises(ValueError):
        build_export_path("../outside.txt")
