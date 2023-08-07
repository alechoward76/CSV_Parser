# CSV_CLI
# Alec Howard
# 08/4/2023

#!/usr/bin/env python3


import argparse
import pandas as pd


def main():
    # Create Parser
    parser = argparse.ArgumentParser(description="A tool for parsing CSV files")

    # Define command line arguments
    parser.add_argument("CSV", type=str, help="Name of csv file to parse")

    parser.add_argument(
        "-n", "--null", action="store_true", help="Flag to remove rows containing NaNs"
    )

    parser.add_argument(
        "-r",
        "--remove",
        action="store_true",
        help="Flag to remove duplicate rows.",
    )
    parser.add_argument(
        "-c",
        "--count",
        nargs=2,
        help="Optional argument to count number of specific entries in a column. Format: 'Column' 'Entry'",
    )

    parser.add_argument(
        "-a",
        "--add",
        nargs="*",
        help="Input columns to add to the output document. Format: 'Column'...",
    )

    # Parse the command line arguments
    args = parser.parse_args()
    try:
        # Read file
        df = pd.read_csv(args.CSV)

        # Remove Duplicate Rows
        if args.remove:
            df = df.drop_duplicates(keep="first")
            print("Duplicate rows (if any) removed!")

        # Remove Rows containing NaNs
        if args.null:
            df = df.dropna()
            print("Rows containing Null values (if any) removed!")

        # Count Entries
        if args.count:
            col = args.count[0]
            entry = args.count[1]

            item_counts = df[col].value_counts()[entry]
            print(str(item_counts) + " Ocurrances")

        # Save columns to doc
        if args.add:
            print("Input Values:", args.add)
            columns = df[args.add]
            columns.to_excel("output.xlsx")
            print("\nCheck your folder ( ͡° ͜ʖ ͡°)\n")

    # Error handle
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nGoodbye! (´^ω^)ノ\n")


if __name__ == "__main__":
    main()
