from pathlib import Path
import argparse
import shutil


def parse_args():
    """ Parse given arguments """
    parser = argparse.ArgumentParser(
        description="Recursively copy folder and sort files by extension",
        usage="<source> [destination]",
        add_help=True
    )

    parser.add_argument(
        "source",
        type=Path,
        required=True,
        help="Source folder"
    )

    parser.add_argument(
        "destination",
        type=Path,
        default="dist",
        help="Destination folder (default: dist)"
    )
    return parser.parse_args()


def process_folders(source: Path, destination: Path):
    try:
        """
        Iterate over all entries within a source
        Call corresponding func recursively
        """
        for entry in source.iterdir():
            if entry == destination:
                continue

            if entry.is_dir():
                process_folders(entry, destination)
            else:
                sort_files(entry, destination)

    except PermissionError:
        print(f"Permission denied: {source}")
        return
    except FileNotFoundError:
        print(f"Path not found: {source}")
        return
    except Exception as e:
        print(f"Error occured while processing {source}: {e}")
        return


def sort_files(file: Path, destination: Path):
    """
    Copy files to destination folders named after their extensions
    Change filename if duplicate detected (filename(1), filename(2), ...)
    """

    file_type = file.suffix[1:] or "other"
    target = destination / file_type

    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

    stem = file.stem
    suffix = file.suffix

    new_name = file.name
    new_path = target / new_name

    counter = 0

    while new_path.exists():
        counter += 1
        new_name = f"{stem}({counter}){suffix}"
        new_path = target / new_name

    try:
        shutil.copy2(file, new_path)

    except Exception as e:
        print(f"Failed to copy {file.name}: {e}")
        return


def main():
    args = parse_args()
    source = Path(args.source).resolve()
    destination = Path(args.destination).resolve()

    if not source.exists() or not source.is_dir():
        print(f"Source folder {source} does not exist or is not a directory")
        return

    try:
        destination.mkdir(parents=True, exist_ok=True)

    except PermissionError:
        print(f"Permission denied: {destination}")
        return
    except FileNotFoundError:
        print(f"Path is not found: {destination}")
        return
    except OSError as e:
        print(f"Directory {destination} can't be created: {e}")
        return
    except Exception as e:
        print(f"Error occured while creating {destination}: {e}")
        return

    process_folders(source, destination)


if __name__ == "__main__":
    main()
