from .policy import can_view_workspace
from .repository import get_document, get_workspace


def view_document(document_id: str, requester_id: str) -> str:
    document = get_document(document_id)
    workspace = get_workspace(document.workspace_id)
    if not can_view_workspace(workspace, requester_id):
        raise PermissionError(f"Requester {requester_id} is not allowed to view document {document_id}")
    return document.content
