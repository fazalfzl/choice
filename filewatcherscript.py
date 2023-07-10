version = 12
import sys
import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--path", help="path to ui file")
    parser.add_argument("-uifile", "--uifile", help="ui file name")
    args = parser.parse_args()

    path = args.path
    uifile = args.uifile
    if path is None:
        print("no path given")
        sys.exit(1)

    path = Path(path).resolve()
    create_init_file_if_not_exist(path)

    command = f"pyuic5 \"{path / uifile}\" -o \"{path / uifile.replace('.ui', '.py')}\""
    print(command)
    os.system(command)


def create_init_file_if_not_exist(path):
    init_file = path / '__init__.py'
    if not init_file.exists():
        init_file.touch()


if __name__ == "__main__":
    main()
