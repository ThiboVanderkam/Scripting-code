import re

phrase = "Collin is 31 jaar, 194 centimeter en woont in Dendermonde"
phrase2 = "Lisa is 26 jaar, 160 centimeter en woont in Dendermonde"


result = re.search(r'\d+', phrase)
print("First occurence = " + result.group())
print("Location = " + str(result.span()))

results = re.findall(r"\d+", phrase)
print(results)

compilerDigits = re.compile(r"\d")

print(compilerDigits.findall(phrase))
print(compilerDigits.findall(phrase2))