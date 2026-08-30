import importlib
import os

import pytest


def _load_vulnerable_app_module():
    package_name = os.environ.get("SECUREAGENT_HOLDOUT_PACKAGE")
    if not package_name:
        raise RuntimeError("SECUREAGENT_HOLDOUT_PACKAGE environment variable is not set")
    module_name = f"{package_name}.case_11.vulnerable_app"
    return importlib.import_module(module_name)


vulnerable_app = _load_vulnerable_app_module()
view_document = vulnerable_app.view_document


def test_collaborator_view_is_allowed():
    assert view_document("document-quarterly", "user-bob") == "Synthetic collaborative quarterly report"


def test_outsider_view_raises_permission_error():
    with pytest.raises(PermissionError):
        view_document("document-quarterly", "user-mallory")
