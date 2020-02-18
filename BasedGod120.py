vals = "1101101 10121 1303 421 302 201 143 146 116 47 96 86 6d 79 79 5a 62 2b 5a 51 28 5a"
vals = vals.split()

output = []

base = 2
for num in vals:
    num = num[::-1]
    dec_num = 0
    exp = 0
    for i in range(len(num)):
        digit = num[i]
        if digit == 'a':
            digit = 10
        elif digit == 'b':
            digit = 11
        elif digit == 'c':
            digit = 12
        elif digit == 'd':
            digit = 13
        elif digit == 'e':
            digit = 14
        elif digit == 'f':
            digit = 15
        else:
            digit = int(num[i])
        digit = digit * (base**exp)
        dec_num = dec_num + digit
        exp +=1
    output.append(dec_num)
    base +=1
    
for char in output:
    print(chr(char), end='')