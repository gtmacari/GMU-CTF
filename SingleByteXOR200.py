encrypted_data = "1b 37 37 33 31 36 3f 78 15 1b 7f 2b 78 34 31 33 3d 78 39 78 28 37 2d 36 3c 78 37 3e 78 3a 39 3b 37 36"
encrypted_data = encrypted_data.split(' ')

for num in range(0, 256):
    print(num, end = ': ')
    for value in encrypted_data:
        print(chr(num ^ int(value, 16)), end='')
    print("")
