def chefway(street,costs,cost,n,k):
    if street == n:
        return cost
    min_cost = 0
    for i in range(1,k+1):
        new_cost = chefway(street+i,cost*costs[street+i],n,k)
        if new_cost < min_cost:
            min_cost = new_cost
    return min_cost

input1 = raw_input().split(' ')
n = int(input1[0])
k = int(input1[1])
costs = map(int,raw_input().split(' '))
print()
