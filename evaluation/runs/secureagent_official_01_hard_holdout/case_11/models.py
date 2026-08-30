from dataclasses import dataclass


@dataclass(frozen=True)
class Workspace:
    workspace_id: str
    owner_id: str
    collaborator_ids: tuple[str, ...]


@dataclass(frozen=True)
class Document:
    document_id: str
    workspace_id: str
    content: str
