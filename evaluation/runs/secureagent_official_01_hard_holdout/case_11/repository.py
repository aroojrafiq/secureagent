from .models import Document, Workspace

_WORKSPACES = {
    "workspace-alpha": Workspace(
        workspace_id="workspace-alpha",
        owner_id="user-alice",
        collaborator_ids=("user-bob",),
    )
}

_DOCUMENTS = {
    "document-quarterly": Document(
        document_id="document-quarterly",
        workspace_id="workspace-alpha",
        content="Synthetic collaborative quarterly report",
    )
}


def get_workspace(workspace_id: str) -> Workspace:
    try:
        return _WORKSPACES[workspace_id]
    except KeyError as exc:
        raise LookupError(f"Workspace not found: {workspace_id}") from exc


def get_document(document_id: str) -> Document:
    try:
        return _DOCUMENTS[document_id]
    except KeyError as exc:
        raise LookupError(f"Document not found: {document_id}") from exc
