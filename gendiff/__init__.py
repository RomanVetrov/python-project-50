from .cli import generate_diff
from .parsers import parse_file


def generate_diff_from_files(file1_path, file2_path):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    return generate_diff(data1, data2)


__all__ = (
    "generate_diff",
    "generate_diff_from_files",
)
