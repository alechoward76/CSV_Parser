# CSV_CLI
# Alec Howard
# 08/4/2023

#!/usr/bin/env python3


import argparse
import pandas as pd


def main():
    # Create Parser
    parser = argparse.ArgumentParser(description="A tool for parsing csv files")

    # Define command line arguments
    parser.add_argument("positional_arg", type=str, help="name of csv file")

    parser.add_argument(
        "-a", "--optional arg", type=str, help="Description of optional arg"
    )

    parser.add_argument(
        "--flag", action="store_true", help="Description of a flag option"
    )
    parser.add_argument(
        "--count",
        nargs=2,
        help="Optional argument to count number of specific entries in a column. Format: 'Column' 'Entry'",
    )

    parser.add_argument(
        "values",
        nargs="*",
        help="Input columns to add to the output document. Format: 'Column'",
    )

    # Parse the command line arguments
    args = parser.parse_args()
    try:
        # Read file
        df = pd.read_csv(args.positional_arg)

        # Add Column to Excel Sheet

        # Access and use the parsed args
        # print("Positional Argument: ", args.positional_arg)

        # print("Flag Option: ", args.flag)

        # Add logic based on parsed args
        if args.flag:
            print("Flag is set!")
        else:
            print("Flag is not set.")

        if args.count:
            col = args.count[0]
            entry = args.count[1]

            item_counts = df[col].value_counts()[entry]
            print(str(item_counts) + " Ocurrances")

        # Save columns to doc
        if args.values:
            print("Input Values:", args.values)
            columns = df[args.values]
            columns.to_excel("output.xlsx")
        """
        if hasattr(args, "optional arg"):
            result = args.optional_arg * 2
            print("Optional Argument: ", args.optional_arg)
            print("Result ", result)
        """
    # Error handle
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
