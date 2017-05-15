startups = open('startups.txt')

seen = set()
unique = []

for name in startups:
    if name not in seen:
        unique.append(name)
        seen.add(name)

print ''.join(map(str, unique))