import re

text = input()
pattern = r"(?P<user>(^|(?<=\s))[a-z0-9]+[._-]*[a-z0-9]+\b)@(?P<host>[a-z]+[\-]*[a-z]+\.[a-z]+[\.a-z]*[a-z])"

matches = re.finditer(pattern, text)

mails = [match.group() for match in matches]

print("\n".join(mails))
