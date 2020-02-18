input = "znfbapp{gurtnhyfunqvgpbzvat}"
output = ""

for i in range(len(input)):
	if i == 7 or i == len(input)-1:
		output = output + input[i]
	elif ord(input[i]) >= ord("n"):
		output = output + chr(ord(input[i])-13)
	else:
		output = output + chr(ord(input[i])+13)

print(output)
