#!/usr/bin/env python3
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    
    parser.add_argument(
        '-f', '--format',
        help='set format of output'
    )

    return parser.parse_args()

def main():
    args = parse_args()
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")
    print(f"Output format: {args.format}")

if __name__ == '__main__':
    main()
