from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    title: str
    created_at: str
