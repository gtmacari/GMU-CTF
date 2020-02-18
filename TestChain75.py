f = open("testChain75.txt","r")

if f.mode == 'r':
	contents = f.read()
	content_lines = contents.split("\n")
	content_lines.remove(content_lines[0])
	content_lines.remove(content_lines[-1])
	ret = -1
	ctr = 1
	while ctr < len(content_lines):
		vals = content_lines[ctr-1].split("\"")
		if int(vals[3]) != ctr:
			ret = ctr;
			break
		ctr+=1
	print(ret)
	#print(content_lines[0].split("\""))
	#3
	#print(content_lines)
	