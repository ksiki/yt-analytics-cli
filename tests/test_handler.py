import pytest

from cli.handler import run
from cli.config import StartCfg


@pytest.fixture
def valid_start_cfg() -> StartCfg:
    return StartCfg(
        files=["test1.csv", "test2.csv"],
        report_type="clickbait"
    )


@pytest.fixture
def files_is_null_start_cfg() -> StartCfg:
    return StartCfg(
        files=None,
        report_type="clickbait"
    )


@pytest.fixture
def files_is_empty_start_cfg() -> StartCfg:
    return StartCfg(
        files=[],
        report_type="clickbait"
    )


@pytest.fixture
def not_exitsts_report_start_cfg() -> StartCfg:
    return StartCfg(
        files=["test1.csv", "test2.csv"],
        report_type="non-existent"
    )


class TestHandler:
    def test_valid_cfg(self, valid_start_cfg) -> None:
        with pytest.raises(FileExistsError):
            assert run(valid_start_cfg)


    @pytest.mark.parametrize(
        "cfg_fixture_name, expectation",
        [
            ("files_is_null_start_cfg", pytest.raises(ValueError)),
            ("files_is_empty_start_cfg", pytest.raises(ValueError)),
            ("not_exitsts_report_start_cfg", pytest.raises(ImportError))
        ]
    )
    def test_not_valid_cfg(self, request, cfg_fixture_name, expectation) -> None:
        cfg = request.getfixturevalue(cfg_fixture_name)
        with expectation:
            assert run(cfg)
