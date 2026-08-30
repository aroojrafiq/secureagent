from .vulnerable_app import view_document


def test_view_document_owner_access():
    assert view_document("document-quarterly", "user-alice") == "Synthetic collaborative quarterly report"
