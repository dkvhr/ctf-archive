import sys

filename = sys.argv[1]
file = open(filename, 'r')
output = open("output.bin", 'wb')

awas = file.read()
awas = awas.split()

if awas[0] != 'awa':
    sys.stderr.write("File does not start with an \'awa\'!\n")
    sys.exit(1)

bin = b''
for awa in awas[1:]:
    if awa == 'awa':
        bin += b'\x00'
        continue
    bin += b'\x00'
    was = int(len(awa[3:])/2)
    bin += b'\x01' * was

output.write(bin)
