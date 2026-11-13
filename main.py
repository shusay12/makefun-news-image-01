import os
import shutil

SOURCE_NAME = "art.png"
OUTPUT_NAME = "entry.png"
OUTPUT_DIR = "/output"


def source_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    destination = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    shutil.copyfile(source_path(), destination)


if __name__ == "__main__":
    main()
