#!/usr/bin/env python3
from .parsers import parse_file
import argparse
import json


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
        choices=["plain", "json"],
        default="plain",
        help="set format of output",
    )
    return parser.parse_args()


def generate_diff(file1_data, file2_data):
    diff = []
    keys = sorted(set(file1_data.keys()).union(file2_data.keys()))
    for key in keys:
        if key not in file2_data:
            diff.append(f"- {key}: {file1_data[key]}")
        elif key not in file1_data:
            diff.append(f"+ {key}: {file2_data[key]}")
        elif file1_data[key] != file2_data[key]:
            diff.append(f"- {key}: {file1_data[key]}")
            diff.append(f"+ {key}: {file2_data[key]}")
    return "\n".join(diff)


def main():
    args = parse_args()
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == "__main__":
    main()
