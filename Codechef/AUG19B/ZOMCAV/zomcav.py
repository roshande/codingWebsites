def increase_radiation(radiation_power):
    n = len(radiation_power)
    radiation_level = [0 for _ in range(n)]
    for i in range(n):
        for j in range(max(i+1-radiation_power[i],0), min(n, i+1+ radiation[i])):
            radiation_level[j]+=1
    return radiation_level

def is_possible(radiation_power, zombies):
    radiation_level = increase_radiation(radiation_power)
    #print(radiation_level)
    n = len(radiation_power)
    return all([r>=z for r,z in zip(radiation_level,zombies)])

for _ in range(int(input())):
    n = int(input())
    radiation = list(map(int, input().split()))
    zombies = list(map(int, input().split()))
    if is_possible(radiation, zombies):
        print("YES")
    else:
        print("NO")
