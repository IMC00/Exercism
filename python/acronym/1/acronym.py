import re


def abbreviate(words: str):
    split_words = [s.strip(" ,_").capitalize()[0] for s in re.split("[ |-]", words) if s != ""]
    return "".join(split_words)
