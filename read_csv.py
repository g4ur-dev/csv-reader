#reading csv
"""
Custom CSV Reader

A lightweight Python implementation of a CSV parser built entirely using
core Python. This program reads CSV files, extracts column headers,
converts numerical values to floating-point numbers, handles missing
values by replacing them with NaN, and stores each row as a dictionary.

Features:
- Reads CSV files using built-in file handling
- Parses column headers
- Converts numeric values to float
- Handles missing values using NaN
- Returns data as a list of dictionaries
- No external libraries required

Author: Gaurang
GitHub: https://github.com/g4ur-dev
"""
import os
os.system('cls')
def parse_header(line1):
    """
    Extracts column names from the first line of a CSV file.

    Args:
        line1 (str): Header line from the CSV file.

    Returns:
        list[str]: List of column names.
    """
    header = line1.strip().split(',')
    return header
def parse_values(data_line):
    """
    Converts a CSV data row into a list of floating-point values.

    Empty fields are converted to NaN.

    Args:
        data_line (str): A row from the CSV file.

    Returns:
        list[float]: Parsed numerical values.
    """
    values = []
    for items in data_line.strip().split(','):
        if items:
            values.append(float(items))
        else:
            values.append(float("nan"))
    return values
def create_dict(header , values):
    """
    Combines headers and values into a dictionary.

    Args:
        header (list[str]): Column names.
        values (list[float]): Corresponding row values.

    Returns:
        dict: Dictionary representing one row of the CSV file.
    """
    formed_dict = {}
    for key , values in zip(header , values):
        formed_dict[key] = values
    return formed_dict
def read_csv(lines):
    """
    Reads CSV content and converts it into a list of dictionaries.

    Args:
        lines (list[str]): Lines read from a CSV file.

    Returns:
        list[dict]: Parsed CSV data where each dictionary
        represents one row.
    """
    if not lines:
        return []
    answer = []
    header = parse_header(lines[0])
    for data_lines in lines[1:]:
        values = parse_values(data_lines)
        answer.append(create_dict(header , values))
    return answer
with open("file reading/csv_reader/loan_template.csv" , "r") as f:
    data = read_csv(f.readlines())
    for row in data:
        print(row)
