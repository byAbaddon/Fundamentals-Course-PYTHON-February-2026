import re

txt = input()
pat = r'\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b'
res = re.findall(pat, txt)
print(' '.join(res))

