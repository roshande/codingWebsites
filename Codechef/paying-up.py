testcases = int(input())
while testcases >0:
	no,money = map(int,input().split())
	notes = []
	for i in range(no):
		notes.append(int(input()))
	#print(notes)
	breaking_point = False
	for i in range(1,1<<no):
		sum = 0
		for j in range(no):
			if i&(1<<j):
				#print(sum)
				sum += notes[j]
		if sum == money:
			print("Yes")
			breaking_point = True
			break
	if not breaking_point:
		print("No")
	testcases -=1
