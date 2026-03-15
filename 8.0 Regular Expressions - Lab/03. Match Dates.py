import re

txt = input()
pat = r'(?P<Day>\d{2})(?P<sep>[./-])(?P<Month>[A-Z][a-z]{2})(?P=sep)(?P<Year>\d{4})'

for x in re.finditer(pat, txt):
  print(f"Day: {x.group('Day')}, Month: {x.group('Month')}, Year: {x.group('Year')}")








