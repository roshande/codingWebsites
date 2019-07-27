# cook your dish here
swaps = ((0,1),(1,2),(0,3),(1,4),(2,5),(3,4),(4,5),(3,6),(4,7),(5,8),(6,7),(7,8))
primes = {3,5,7,11,13,17}

def swap(board,swap):
    b = list(board)
    b[swap[0]],b[swap[1]] = b[swap[1]],b[swap[0]]
    return tuple(b)

def init_db():
    board = (1,2,3,4,5,6,7,8,9)
    bfs = [board]
    seen = {board:0}
    for board in bfs:
        for s in [(a,b) for a,b in swaps if board[a] + board[b] in primes]:
            newboard = swap(board,s)
            if newboard in seen:
                continue
            #print(type(newboard))
            bfs.append(newboard)
            seen[newboard] = seen[board] + 1
    return seen

seen = init_db()
for _ in range(int(input())):
    input()
    board = [0]*9
    for i in range(0,9,3):
        board[i],board[i+1],board[i+2] = list(map(int,input().split()))
    #print(board)
    if not tuple(board) in seen:
        print(-1)
    else:
        print(seen[tuple(board)])
