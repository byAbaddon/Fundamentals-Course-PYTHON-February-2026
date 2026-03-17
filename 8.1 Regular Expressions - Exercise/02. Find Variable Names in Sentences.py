import re

txt = input()
res = re.findall(r'(?<![A-Za-z0-9_])_([A-Za-z0-9]+)\b'   ,txt)
print(','.join(res))