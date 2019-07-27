for _ in range(int(input())):
    n = int(input())
    names = []
    name_map = {}
    for _ in range(n):
        firstname,lastname = input().split()
        if firstname in name_map.keys():
            name_map[firstname].append(lastname)
        else:
            name_map[firstname] = [lastname]
        names.append([firstname, lastname])
    for firstname,lastname in names:
        if len(name_map[firstname]) > 1:
            print(firstname, lastname)
        else:
            print(firstname)

