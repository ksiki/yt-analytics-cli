import logging
import sys
import argparse
from typing import Final

import handler
from config import (
    StartCfg,
    FILES_ARG,
    FILES_ARG_CFG,
    REPORT_ARG,
    REPORT_ARG_CFG
)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger: Final[logging.Logger] = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(FILES_ARG, **FILES_ARG_CFG)
    parser.add_argument(REPORT_ARG, **REPORT_ARG_CFG)

    args = parser.parse_args()
    cfg = StartCfg(
        files=args.files,
        report_type=args.report
    )

    try:
        handler.run(cfg)
    except Exception as e:
        logger.error(f"{e}")
    finally:
        exit()


def exit() -> None:
    logger.info("Exit")
    sys.exit(130)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
