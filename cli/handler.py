import importlib

from config import StartCfg
from utils.presenter import write_data


def run(cfg: StartCfg) -> None:
    if cfg.files is None:
        raise ValueError(f"{__name__}: files is null")
    if len(cfg.files) < 1:
        raise ValueError(f"{__name__}: files list is empty")

    try:
        module_name = f"reports.{cfg.report_type}_report"
        report_module = importlib.import_module(module_name)
        report_class = getattr(report_module, f"{cfg.report_type.capitalize()}Report")
        
        generator = report_class()
        data = generator.generate(cfg.files)
        write_data(data)
    except ImportError:
        raise ImportError(f"Report type '{cfg.report_type}' not exists")
