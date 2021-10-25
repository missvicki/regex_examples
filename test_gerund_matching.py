"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
pattern = r"(?=\w+(?=(?<!y)y(?!y))|\w+(?<=[aieou])+ing)\w+"
# ^^^ ADD YOUR PATTERN HERE ^^^ #
# raise NotImplementedError("Add your pattern to the test file.")

test_case = [
    ("harry loves to sing while showering.", True),
    ("i am going to the market", True),
    ("are you coming to town with me?", True),
    ("the children were singing to the music while doing jumping jacks", True),
    ("14 is on the numbering scale", True),
    ("14 is a number", False),
    ("you are very annoying", True),
    ("ping me when you are done", False),
    ("the cat is dying", True),
    ("ing you", False),
    ("yying you", False)
]

@pytest.mark.parametrize("string,matches", test_case)
def test_gerund_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string) is not None) == matches
