from reports.base import BaseReport
from utils.data_formatter import extract_columns
from utils.file_reader import read_files


class ClickbaitReport(BaseReport):
    def __init__(self):
        super().__init__()
        self.__needed_columns = ["title", "ctr", "retention_rate"]
        self.__ctr_min_filter = 15
        self.__retention_rate_max_filter = 40

    def generate(self, files: list[str]) -> list[dict[str, str]]:
        needed_data = []
        
        file_reader = read_files(
            files=files
        )
        for data_from_file in file_reader:
            filtered_data = extract_columns(
                data=data_from_file,
                needed_columns=self.__needed_columns
            )
            for row in filtered_data:
                print(row)
                ctr = float(row.get(
                    "ctr", 
                    self.__ctr_min_filter
                ))
                retention_rate = float(row.get(
                    "retention_rate", 
                    self.__retention_rate_max_filter
                ))
                if ctr > self.__ctr_min_filter and retention_rate < self.__retention_rate_max_filter:
                    needed_data.append(row)

        needed_data.sort(
            key=lambda x: float(x.get("ctr", 0)),
            reverse=True
        )
        return needed_data
