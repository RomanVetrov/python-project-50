#!/usr/bin/env python3
import argparse

from gendiff import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        choices=["stylish", "plain"],
        default="stylish",
        help="set format of output",
    )
    return parser.parse_args()


# def generate_diff(file1_data, file2_data):
#     diff = []
#     keys = sorted(set(file1_data.keys()).union(file2_data.keys()))
#     for key in keys:
#         if key not in file2_data:
#             diff.append(f"- {key}: {file1_data[key]}")
#         elif key not in file1_data:
#             diff.append(f"+ {key}: {file2_data[key]}")
#         elif file1_data[key] != file2_data[key]:
#             diff.append(f"- {key}: {file1_data[key]}")
#             diff.append(f"+ {key}: {file2_data[key]}")
#     return "\n".join(diff)


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
