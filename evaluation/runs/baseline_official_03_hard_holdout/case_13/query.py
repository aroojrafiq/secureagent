_VALID_SORT_FIELDS = {
    "title": "title",
    "created_at": "created_at",
}


def build_report_query(sort_by: str) -> str:
    normalized_sort = sort_by.strip()
    if normalized_sort not in _VALID_SORT_FIELDS:
        raise ValueError(f"Unsupported sort field: {sort_by!r}")

    order_by = _VALID_SORT_FIELDS[normalized_sort]
    return f"""
SELECT title, created_at
FROM reports
WHERE owner_id = ?
ORDER BY {order_by}
"""
