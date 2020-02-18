#The letters of the alphabet are flipped. (a-->z b-->y etc.)

input = "wlmg_wl_gsrh_nzmfzoob"
output = ""

for i in range(len(input)):
    pos = ord(input[i])-97
    if input[i] == "_":
        output = output + "_"
    else:
        new_pos = 25-pos
        output = output + chr(new_pos + 97)

print(output)

'''
a b c d e f g h i j k l m
z y x w v u t s r q p o n
'''
#dont_do_this_manually