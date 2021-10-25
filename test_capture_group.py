"""Test group-capture-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
pattern = r"\(([^?]|\?P)+\)"
# ^^^ ADD YOUR PATTERN HERE ^^^ #
# raise NotImplementedError("Add your pattern to the test file.")



test_case = [
    ("([ˆ@]+)@(?:[ˆ@]+.[ˆ@]+)", True),
    ("(?P<name>)", True),
    ("(?P=letter)", True),
    ("([])", True),
    ("(abc)", True),
    ("(?=name)", False),
    ("(())", True),
    ("()", True),
    ("(.)\1", True),
    ("\b\w*(.)", True),
    ("(?...)", False)
]

@pytest.mark.parametrize("string,matches", test_case)
def test_capture_group(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string) is not None) == matches
