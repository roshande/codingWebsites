def favsubseq(string,start=0,end=None):
    if end is None:
        end=len(string)-1
    countb = string.count("b",start,end)
    if countb==0:
        return 0
    result = 2**countb -1
    firsta = string.find("a",start+1,end-1)
    lastc = string.rfind("c",start+1,end-1)
    if firsta == -1 and lastc != -1:
            result = result + 2*favsubseq(string,start,lastc)
    elif lastc==-1:
        result = result + 2*favsubseq(string,firsta,end)
    else:
        result = result + 2*(favsubseq(string,firsta,end) + favsubseq(string,start,lastc))
    return result%(7+1E9)

string = input()
#print(string)

#cleaning
firsta = string.find('a')
lastc = string.rfind('c')
if -1 in [firsta,lastc]:
    print(0)
else:
    result = favsubseq(string,start=firsta,end=lastc)
    print(int(result))
