known_pt = "uiuctf{"

with open("ct", "rb") as f:
    data = f.read()

keys = []
for a in range(len(known_pt)):
    for b in range(33, 127):
        if chr(data[a] ^ b) == known_pt[a]:
            keys.append(b)
            break

for i in range(33, 127):
    if chr(data[47] ^ i) == '}':
        keys.append(i)
        break

for key in keys:
    print(chr(key), end='')
