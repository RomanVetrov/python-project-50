import json

from .cli import generate_diff


def generate_diff_from_files(file1_path, file2_path):
    with open(file1_path, "r") as f1:
        data1 = json.load(f1)
    with open(file2_path, "r") as f2:
        data2 = json.load(f2)
    return generate_diff(data1, data2)


__all__ = (
    "generate_diff",
    "generate_diff_from_files",
)
