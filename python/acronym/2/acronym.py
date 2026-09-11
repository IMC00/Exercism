import re


def abbreviate(words: str):
    return "".join([s.strip(" ,_").capitalize()[0] for s in re.split("[ |-]", words) if s != ""])
