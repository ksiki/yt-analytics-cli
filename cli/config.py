from typing import Any, Final
from dataclasses import dataclass


@dataclass
class StartCfg:
    files: list[str]
    report_type: str


FILES_ARG: Final[str] = "--files"
FILES_ARG_CFG: Final[dict[str, Any]] = {
    "nargs": "+",
    "required": True,
    "help": "Files list"
}


REPORT_ARG: Final[str] = "--report"
REPORT_ARG_CFG: Final[dict[str, Any]] = {
    "choices": ["clickbait"],
    "required": True,
    "help": "Report type"
}
