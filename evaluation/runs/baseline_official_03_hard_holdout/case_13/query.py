# THIS IS AN INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE AND MUST NEVER BE USED IN PRODUCTION.
def build_report_query(sort_by: str) -> str:
    return f"""
SELECT title, created_at
FROM reports
WHERE owner_id = ?
ORDER BY {sort_by}
"""
