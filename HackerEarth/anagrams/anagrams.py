
def areAnagrams(str1,str2):
    hashaz = [0] * 26
    for ch in str1:
        hashaz[ord(ch)-97] = hashaz[ord(ch)-97] +1
    for ch in str2:
        hashaz[ord(ch)-97] = hashaz[ord(ch)-97] -1
    if sum(hashaz)==0:
        return True
    else:
        return False
        
n = int(input().strip())
str1 = input()
str2 = input()
if areAnagrams(str1,str2):
    print("YES")
else:
    print("NO")
