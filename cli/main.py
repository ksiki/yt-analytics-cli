import sys
import argparse

import handler
from config import (
    StartCfg,
    FILES_ARG,
    FILES_ARG_CFG,
    REPORT_ARG,
    REPORT_ARG_CFG
)


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
        print(f"\nError-{e}")
    finally:
        exit()


def exit() -> None:
    print("\nExit")
    sys.exit(130)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
