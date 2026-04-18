from reports.base import BaseReport


class ClickbaitReport(BaseReport):
    def __init__(self):
        super().__init__()
        self.__needed_columns = ["title", "ctr", "retention_rate"]
        self.__ctr_min_filter = 15
        self.__retention_rate_max_filter = 40

    def generate(self, files: list[str]) -> list[dict[str, str]]:
        data = []
        
        file_reader = self._read_files(
            files, 
            self.__needed_columns
        )
        for data_from_file in file_reader:
            for i, row in enumerate(data_from_file):
                ctr = float(row.get(
                    "ctr", 
                    self.__ctr_min_filter
                ))
                retention_rate = float(row.get(
                    "retention_rate", 
                    self.__retention_rate_max_filter
                ))
                if ctr > self.__ctr_min_filter and retention_rate < self.__retention_rate_max_filter:
                    data.append(data_from_file[i])

        data.sort(
            key=lambda x: float(x.get("ctr", 0)), 
            reverse=True
        )
        return data