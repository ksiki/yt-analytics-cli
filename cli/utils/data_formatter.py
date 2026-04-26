from typing import Any


def extract_columns(data: list[dict[str, Any]], needed_columns: list[str]) -> list[dict[str, Any]]:
    result = []
    for row in data:
        filtered_row = {key: row[key] for key in needed_columns}
        result.append(filtered_row)
    return result
