[print(s[i:i+2]) for s in input().split() for i in range(len(s)-1) if s[i] == ':']
# [print(s[i:i+2]) for s in input().split() for i, ch in enumerate(s[:-1]) if ch == ':']

