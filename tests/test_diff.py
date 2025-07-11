import os
import textwrap

from gendiff import generate_diff_from_files


HERE = os.path.dirname(__file__)
FILE1 = os.path.join(HERE, "../file1.json")
FILE2 = os.path.join(HERE, "../file2.json")

EXPECTED = textwrap.dedent(
    """\
    - follow: False
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True"""
)


def test_generate_diff_plain():
    result = generate_diff_from_files(FILE1, FILE2)
    assert result == EXPECTED
