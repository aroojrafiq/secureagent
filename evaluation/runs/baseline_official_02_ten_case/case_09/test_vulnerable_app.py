import pytest

from .vulnerable_app import view_report


def test_view_report_for_owner_access():
    assert view_report("report-alice", "user-alice") == "Synthetic quarterly summary"


def test_view_report_rejects_non_owner():
    with pytest.raises(PermissionError):
        view_report("report-alice", "user-bob")
