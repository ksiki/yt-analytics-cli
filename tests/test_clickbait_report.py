import os
import pytest
from pathlib import Path

from cli.reports.clickbait_report import ClickbaitReport


@pytest.fixture
def temp_csv() -> list[str]:
    test_path = Path(__file__).resolve().parent / "test_file.csv"

    content = "title,ctr,retention_rate,test_column\n"
    content += "Video 1,15.1,10.0,text1\n"
    content += "Video 2,30.0,39.9,text2\n"
    content += "Video 3,40.0,40.0,text3\n"
    content += "Video 4,15.0,30.0,text4"
    test_path.write_text(content)

    return [str(test_path)]


@pytest.fixture
def not_exists_path() -> list[str]:
    return ["test1.csv"]


@pytest.fixture
def clickbait_report() -> ClickbaitReport:
    return ClickbaitReport()


class TestClickbaitReport:
    def test_not_exists_path(self, clickbait_report, not_exists_path) -> None:
        with pytest.raises(FileExistsError):
            assert clickbait_report.generate(not_exists_path)

    def test_exist_path(self, clickbait_report, temp_csv) -> None:
        data = clickbait_report.generate(temp_csv)

        assert len(data) == 2
        assert data[0]["title"] == "Video 2"
        assert data[1]["title"] == "Video 1"

        os.remove(temp_csv[0])
