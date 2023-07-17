# Creating a Command Line Interface for smoother user experience

# CSV_CLI
import argparse
from pathlib import Path
import datetime

# create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("path")


# Add args
parser.add_argument("-l", "--long", action="store_true")


args = parser.parse_args()

# Setup target directory of script
target_dir = Path(args.path)

# alert if directory is nonexistent
if not target_dir.exists():
    print("The target does not exist")
    raise SystemExit(1)


# build output
def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size

        date = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


# Print name of dir
for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
