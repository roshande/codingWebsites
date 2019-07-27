for _ in range(int(input())):
	l = int(input())
	report = input()
	headstart = False
	for ch in report:
		if ch == '.':
			continue
		elif ch == 'H' and not headstart:
			headstart = True
		elif ch == 'T' and headstart:
			headstart = False
		else:
			headstart = True
			break
	if not headstart:
		print("Valid")
		continue
	print("Invalid")
