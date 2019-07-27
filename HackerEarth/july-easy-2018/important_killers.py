def add_imps(imps,P):
    for x in range(imps[-1],P+1):
        notimp = False
        for imp in imps:
            if x % imp**2 == 0:
                notimp = True
                break
        if not notimp :
            imps.append(x)
imps = [2,3,5,6,7,10]
add_imps(imps,50)
print(imps)
alive  = imps[:]
print(len(alive))
