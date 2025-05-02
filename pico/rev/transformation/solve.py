file = open("enc", "r")
a = file.read()

for i in range(0, len(a)):
    print(chr(ord(a[i]) >> 8 ), end="")
    print(chr(a[i].encode('utf-16be')[-1]), end="")

