# Alec Howard
# 06/15/2023
# CSV Parser

# Imports
import os
import pandas as pd

while 1 == 1:
    # Input Username and File Name
    try:
        print("Enter Username For File Path: ")
        userName = input()
        print("\nEnter Name of CSV File From Documents Folder (including extension): ")
        fileName = input()

        # Create Dataframe from input csv file
        df = pd.read_csv(r"C:\Users\\" + userName + "\\Documents" + "\\" + fileName)
        break
    except:
        print("INVALID PATH: Retry \n")


# column List I want parsed out
selected_columns = []

# Start Main While Loop
while 1 == 1:
    print("\nEnter a Number to Select an Option: \n")
    print("1. Add Column")
    print("2. Count Occurrences of an Item in Specific Column")
    print("3. Exit & Export")
    userInput = input()

    # Add Column to Excel Sheet
    if userInput == "1":
        try:
            # show all columns
            print("\nColumns: \n")
            print(df.columns)

            # Enter Column to Select
            print("\n")
            print("Enter Column Name to Add \n")
            columnName = input()
            testValid = df[columnName]
            selected_columns.append(columnName)
            print("\nSelected Column(s) " + str(selected_columns) + "\n")
        except:
            print("INVALID COLUMN NAME\n")

            print("INVALID SELECTION: Reselect Columns \n")

    # Count occurences of a specific item in a specific column
    elif userInput == "2":
        try:
            # Select Column to Search
            print("\nColumns: \n")
            print(df.columns)
            print("\nEnter Column Name to Search: \n")
            columnName = input()

            # Drop Duplicates and NAN when displaying item options in column
            print("\n")
            print(df[columnName].drop_duplicates().dropna())
            print("\n")

            # Selecting Item to search for in column
            print("\nEnter Item to Search: \n")
            item_to_search = input()
            item_counts = df[columnName].value_counts()[item_to_search]
            print(item_to_search + ": " + str(item_counts) + " Occurrences")
            print("\n")
            print("Quit Without Exporting? (y/n) \n")
            userChoice = input()
            if userChoice == "y":
                break
        except:
            print("INVALID: Retry\n")
    # Exit & Export
    elif userInput == "3":
        try:
            # pull dataframe data from the selected columns, choice of dropping data
            print("\nWould you like to drop duplicates and NANs? (y/n) \n")
            choice = input()
            if choice == "y":
                subset_data = df[selected_columns].drop_duplicates().dropna()
            elif choice == "n":
                subset_data = df[selected_columns]

            print(subset_data)
            print("\n")

            print("Would You Like to Export to Excel? (y/n)\n")
            choose = input()
            if choose == "y":
                # Export subset data to excel file
                print("\nEnter xlsx File Name to Output to (including extension) ")
                outputFile = input()
                subset_data.to_excel(
                    r"C:\Users\amh3097\Documents\\" + outputFile, index=False
                )
                print("\nCheck your Documents Folder ( ͡° ͜ʖ ͡°)\n")
                break
            else:
                print("\nGoodbye! (´^ω^)ノ\n")
                break

        except:
            # Reset Selection Process if an Invalid Column is Provided
            selected_columns = []

    # Invalid Option
    else:
        print("Invalid Option \n")
# END WHILE LOOP