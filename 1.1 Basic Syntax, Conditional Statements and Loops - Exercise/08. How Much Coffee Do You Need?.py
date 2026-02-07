coffe = 0

for s in [x for x in iter(input, 'END')]:

    if s.lower() in ['cat', 'dog', 'movie', 'coding']:
        coffe += 2 if s.upper() == s else 1

print('You need extra sleep' if coffe > 5 else coffe)
