import re

pattern = r"sand|water|fish|sun"
result = re.findall(pattern, input().lower())
print(len(result))
