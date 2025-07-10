import json
from .cli import generate_diff

def generate_diff_from_files(file1_path, file2_path):
    
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)
    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    
    return generate_diff(data1, data2)