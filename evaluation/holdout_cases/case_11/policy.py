from .models import Workspace


def can_view_workspace(workspace: Workspace, requester_id: str) -> bool:
    if requester_id == workspace.owner_id:
        return True
    if requester_id in workspace.collaborator_ids:
        return True
    return False
