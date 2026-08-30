from .repository import get_document, get_workspace

# INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: THIS MUST NEVER BE USED IN PRODUCTION.

def view_document(document_id: str, requester_id: str) -> str:
    document = get_document(document_id)
    get_workspace(document.workspace_id)
    return document.content
