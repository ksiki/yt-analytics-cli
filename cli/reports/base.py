import os
import csv
from abc import ABC, abstractmethod
from typing import Any, Final, Generator

CSV_FORMAT: Final[str] = ".csv"


class BaseReport(ABC):
    @abstractmethod
    def generate(self) -> list[dict[str, str]]:
        pass    

    def _read_files(self, files: list[str], needed_columns: list[str] = []) -> Generator[list, None, None]:
        for path in files:
            if not path.endswith(CSV_FORMAT):
                path += CSV_FORMAT
            if not os.path.exists(path):
                raise FileExistsError(f"{__name__}: path '{path}' is not exist")
            
            with open(path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                if len(needed_columns) > 0:
                    data = self.__extract_columns(reader, needed_columns)
                    yield data
                else:
                    yield list(reader)
        
    def __extract_columns(self, reader: csv.DictReader, needed_columns: list[str]) -> list[dict[str, Any]]:
        data = []
        for row in reader:
            filtered_row = {key: row[key] for key in needed_columns}
            data.append(filtered_row)
        return data