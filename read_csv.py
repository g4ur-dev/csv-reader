#reading csv
import os
os.system('cls')
def parse_header(line1):
    header = line1.strip().split(',')
    return header
def parse_values(data_line):
    values = []
    for items in data_line.strip().split(','):
        if items:
            values.append(float(items))
        else:
            values.append(float("nan"))
    return values
def create_dict(header , values):
    formed_dict = {}
    for key , values in zip(header , values):
        formed_dict[key] = values
    return formed_dict
def read_csv(lines):
    if not lines:
        return []
    answer = []
    header = parse_header(lines[0])
    for data_lines in lines[1:]:
        values = parse_values(data_lines)
        answer.append(create_dict(header , values))
    return answer
with open("file reading/loan_template.csv" , "r") as f:
    print(read_csv(f.readlines()))