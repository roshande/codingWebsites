def max_heights():
	n = int(input())
	heights = list(map(int,input().split()))
	max_area = 0
	for i in range(n):
		for j in range(i+1,n):
			area = (j-i)*min(heights[i:j+1])
			if max_area < area:
				max_area = area
	print(max_area)

for _ in range(int(input())):
	max_heights()
