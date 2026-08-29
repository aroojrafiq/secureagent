from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    report_id: str
    owner_id: str
    content: str
