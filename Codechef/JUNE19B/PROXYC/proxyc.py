def num_of_proxies(attendance):
    D = len(attendance)
    req_attendance = round(D*0.75)
    present = attendance.count('P')
    if present >= req_attendance:
        return "0"
    allowed_proxies = 0
    if D <= 4:
        if present < 3:
            return "-1"
        return "0"
    for i in range(2,D-2):
        if attendance[i] == 'A' \
            and (attendance[i-1] == 'P' or attendance[i-2] == 'P') \
            and (attendance[i+1] == 'P' or attendance[i+2] == 'P'):
            allowed_proxies += 1
            if req_attendance == (present+allowed_proxies):
                break
    else:
        return "-1"
    #print(allowed_proxies)
    #if req_attendance > (present + allowed_proxies):
    #    return "-1"
    return allowed_proxies #req_attendance - present

for _ in range(int(input())):
    l = int(input())
    attendance = input()
    print(num_of_proxies(attendance))
