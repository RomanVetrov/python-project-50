import os
from gendiff import generate_diff

HERE = os.path.dirname(__file__)
FILE1 = os.path.join(HERE, "test_data", "file1.json")
FILE2 = os.path.join(HERE, "test_data", "file2.json")
FILE1_YAML = os.path.join(HERE, "test_data", "file1.yaml")
FILE2_YAML = os.path.join(HERE, "test_data", "file2.yaml")
NESTED1 = os.path.join(HERE, "test_data", "nested1.json")
NESTED2 = os.path.join(HERE, "test_data", "nested2.json")

EXPECTED_NESTED = """
{
common: {
  + follow: false
    setting1: Value 1
  - setting2: 200
  - setting3: true
  + setting3: null
  + setting4: blah blah
  + setting5: {
            key5: value5
        }
    setting6: {
        doge: {
          - wow: 
          + wow: so much
            }
        key: value
      + ops: vops
        }
    }
group1: {
  - baz: bas
  + baz: bars
    foo: bar
  - nest: {
            key: value
        }
  + nest: str
    }
- group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
+ group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
""".strip()

EXPECTED = """
{
- follow: false
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}
""".strip()


def test_generate_diff_plain():
    result = generate_diff(FILE1, FILE2)
    assert result.strip() == EXPECTED.strip()


def test_generate_diff_yaml():
    result = generate_diff(FILE1_YAML, FILE2_YAML)
    assert result.strip() == EXPECTED.strip()


def test_generate_diff_json_yaml():
    result = generate_diff(FILE1, FILE2_YAML)
    assert result.strip() == EXPECTED.strip()


def test_generate_diff_yaml_json():
    result = generate_diff(FILE1_YAML, FILE2)
    assert result.strip() == EXPECTED.strip()


def test_generate_diff_nested():
    result = generate_diff(NESTED1, NESTED2)
    assert result.strip() == EXPECTED_NESTED