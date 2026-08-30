def build_report_query(sort_by: str) -> str:
    if sort_by == "title":
        return """
SELECT title, created_at
FROM reports
WHERE owner_id = ?
ORDER BY title ASC
"""
    if sort_by == "created_at":
        return """
SELECT title, created_at
FROM reports
WHERE owner_id = ?
ORDER BY created_at ASC
"""
    raise ValueError(f"Unsupported sort key: {sort_by}")
