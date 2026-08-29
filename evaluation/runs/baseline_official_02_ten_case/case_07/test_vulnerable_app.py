from .vulnerable_app import extract_backup_archive


class FakeArchive:
    """Minimal archive stub that records arguments passed to extractall."""

    def __init__(self):
        self.last_kwargs = None

    def extractall(self, **kwargs):
        self.last_kwargs = kwargs


def test_extract_backup_archive_functional_behavior():
    """Functional test: the archive is extracted to the requested destination and returns None."""
    archive = FakeArchive()

    result = extract_backup_archive(archive, "synthetic-output")

    assert result is None
    assert archive.last_kwargs is not None
    assert archive.last_kwargs["path"] == "synthetic-output"


def test_extract_backup_archive_uses_safe_filter():
    """Security test: a repaired implementation should pass filter='data' to extractall."""
    archive = FakeArchive()

    extract_backup_archive(archive, "synthetic-output")

    assert archive.last_kwargs["filter"] == "data"
