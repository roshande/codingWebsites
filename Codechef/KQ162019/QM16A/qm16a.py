for _ in range(int(input())):
    sent1 = set(input().split())
    sent2 = set(input().split())
    for word in sent1:
        if word in sent2:
            print("Yes")
            break
    else:
        print("No")


