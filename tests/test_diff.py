import os
from gendiff import generate_diff

HERE = os.path.dirname(__file__)
FILE1 = os.path.join(HERE, "test_data", "file1.json")
FILE2 = os.path.join(HERE, "test_data", "file2.json")
FILE1_YAML = os.path.join(HERE, "test_data", "file1.yaml")
FILE2_YAML = os.path.join(HERE, "test_data", "file2.yaml")
NESTED1 = os.path.join(HERE, "test_data", "nested1.json")
NESTED2 = os.path.join(HERE, "test_data", "nested2.json")

EXPECTED_PLAIN = (
    "Property 'follow' was removed\n"
    "Property 'proxy' was removed\n"
    "Property 'timeout' was updated. From 50 to 20\n"
    "Property 'verbose' was added with value: true"
)

EXPECTED_PLAIN_NESTED = (
    "Property 'common.follow' was added with value: false\n"
    "Property 'common.setting2' was removed\n"
    "Property 'common.setting3' was updated. From true to null\n"
    "Property 'common.setting4' was added with value: 'blah blah'\n"
    "Property 'common.setting5' was added with value: [complex value]\n"
    "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
    "Property 'common.setting6.ops' was added with value: 'vops'\n"
    "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
    "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
    "Property 'group2' was removed\n"
    "Property 'group3' was added with value: [complex value]"
)

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


def test_generate_diff_plain_format():
    assert generate_diff(FILE1, FILE2, "plain").strip() == EXPECTED_PLAIN


def test_generate_diff_plain_nested():
    assert generate_diff(NESTED1, NESTED2, "plain").strip() == (
    EXPECTED_PLAIN_NESTED
    )