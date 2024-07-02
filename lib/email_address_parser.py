import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        filtered = re.compile(r'\w+\.?\w+@\w+\.[A-z]+').findall(self.string)
        st = set(filtered)
        return sorted(list(st))