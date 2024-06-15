import re

pattern = r"(?<=\s_)[A-Za-z0-9]+\b"

text = input()

matches = re.finditer(pattern, text)
variables = [match.group() for match in matches]

print(",".join(variables))
