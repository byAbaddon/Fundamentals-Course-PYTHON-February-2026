import re

txt, w= input(), input()
res = re.findall(rf'\b{w}\b', txt, re.IGNORECASE)
print(len(res))