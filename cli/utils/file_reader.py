import csv
import os
from typing import Final, Generator


CSV_FORMAT: Final[str] = ".csv"


def read_files(files: list[str]) -> Generator[list, None, None]:
    for path in files:
        if not path.endswith(CSV_FORMAT):
            path += CSV_FORMAT
        if not os.path.exists(path):
            raise FileExistsError(f"{__name__}: path '{path}' is not exist")
        
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            yield list(reader)
