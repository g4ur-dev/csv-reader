# CSV Reader

A custom CSV parser built entirely with core Python without using the built-in `csv` module.

## Features

- Reads CSV files
- Extracts column headers
- Converts numeric values to float
- Handles missing values using NaN
- Returns a list of dictionaries

## Example

Input:

Age,Salary
21,50000
25,60000

Output:

[
    {'Age': 21.0, 'Salary': 50000.0},
    {'Age': 25.0, 'Salary': 60000.0}
]