# CSV_CLI
# Alec Howard
# 08/4/2023

#!/usr/bin/env python3


import argparse
import pandas


def main():
    # Create Parser
    parser = argparse.ArgumentParser(description="A tool for parsing csv files")

    # Define command line arguments
    parser.add_argument("positional_arg", type=str, help="name of csv file")

    # What is the difference between these two?v
    """
    parser.add_argument(
        "-o", "--optional arg", type=int, default=0, help="Description of optional arg"
    )
    """
    parser.add_argument(
        "--flag", action="store_true", help="Description of a flag option"
    )

    # Parse the command line arguments
    args = parser.parse_args()
    try:
        # Access and use the parsed args
        print("Positional Argument: ", args.positional_arg)

        print("Flag Option: ", args.flag)

        # Add logic based on parsed args
        if args.flag:
            print("Flag is set!")
        else:
            print("Flag is not set.")
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
