def ispossible(book1,book2,m=0,n=0):
    if m==len(book1) and n==len(book2):
        return True
    elif book1[m]==book2[n]:
        return ispossible(book1,book2,m+1,n+1)
    else:
        if book1[m]=='*':
            return ispossible(book1,book2,m,n+1) or ispossible(book1,book2,m,n+1) or ispossible(book1,book2,m,n+3) or ispossible(book1,book2,m,n+4)
        elif book2[n]=='*':
            return ispossible(book1,book2,m+1,n) or ispossible(book1,book2,m+2,n) or ispossible(book1,book2,m+3,n) or ispossible(book1,book2,m+4,n)
        else:
            return False
n = int(input())
for i in range(1,n+1):
    book1 = input()
    book2 = input()
    if ispossible(book1,book2):
        print("Case #%d: TRUE"%i)
    else:
        print("Case #%d: FALSE"%i)
