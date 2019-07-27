test = int(input())
while test > 0:
	string = (input())
	outputUpp = []
	outputLow = []
	for ch in string:
		if ch.islower():
			outputLow.append(ch)
		elif ch.isupper():
			outputUpp.append(ch)
	outout = "".join(outputUpp) + "".join(outputLow)
	print(outout)
	test -=1
