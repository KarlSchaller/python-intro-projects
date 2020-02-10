#Karl Schaller

import re

tuRegex = re.compile(r"\btu[a-z]\d{5}@temple\.edu\b")
print(tuRegex.findall("tug85861@temple.edu"))
print(tuRegex.findall("tuf95861@temple.edu"))
print(tuRegex.findall("tux85871@temple.edu"))
print(tuRegex.findall("tff8587@temple.edu"))
print(tuRegex.findall("tug85261@temple.com"))
print(tuRegex.findall("nigerian.scammer@419.com"))

aliasRegex = re.compile(r"\b[a-zA-Z0-9][a-zA-Z0-9_\-.]*[a-zA-Z0-9]@temple\.edu\b")
print(aliasRegex.findall("ana@temple.edu"))
print(aliasRegex.findall("a-n@temple.edu"))
print(aliasRegex.findall("andrew.Is.Not_The-1.3.3.7.est@temple.edu"))
print(aliasRegex.findall("andrew.rosen@temple.edu"))

dateRegex = re.compile(r"\b\d(\d)?(/|-)\d(\d)?(/|-)\d\d(\d)?(\d)?\b")
print(dateRegex.search("03-02-2019"))
print(dateRegex.search("03/02/2019"))
print(dateRegex.search("3/2/2019"))
print(dateRegex.search("3/2/19"))
