from .diff_builder import build_diff
from .formatters.json import format_json
from .formatters.plain import format_plain
from .formatters.stylish import format_stylish
from .parsers import parse_file


def generate_diff(file1_path, file2_path, format_name="stylish"):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    diff = build_diff(data1, data2)
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


__all__ = (
    "generate_diff",
)
