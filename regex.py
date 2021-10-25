"""Try out regular expressions"""
import re

strings = [
    "arg",
    "aaaarrrrg",
    "rrg",
    "superman",
    "man",
    "batman",
    "superbatsuperbatman",
    "1600 Pennsylvania Avenue",
    "401 Chapel Drive",
    "3624  Hillsborough Road",
    "32 442 asd",
    "123 hello world",
    "He Him",
    "hello world",
    "goodbye hello",
    "shellow",
    "Patrick Wang",
    "Patrick Swayze",
    "Jeremy Wang"
]

# pattern = r"a+r+g"
# pattern = r"a*r+g"
# pattern = r"(super|bat)*man"
# pattern = r"[1-9][0-9]*( [A-Z][a-z]*){2}"
# pattern = r"[1-9]\d*(\s+[A-Z][a-z]*){2}"
# pattern = r"\bhello\b"
pattern = r"(?<=Patrick )\w+" #match last names of famous patricks : insists patrick be in the match but don't include it

for string in strings:
    # output = re.fullmatch(pattern, string)
    output = re.findall(pattern, string) # use to match block and group extensions
    print(string, output)

