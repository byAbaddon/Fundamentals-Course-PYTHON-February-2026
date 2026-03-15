import re

txt = input()
pat = r'\+359 [2] \d{3} \d{4}\b|\+359-[2]-\d{3}-\d{4}\b'
res = re.findall(pat, txt)
print(', '.join(res))



