def solve(board=[], row=0, N=8):
    if row == N:
        for r in board:
            print(' '.join('Q' if i==r else '.' for i in range(N)))
        print()
        return
    for col in range(N):
        if all(c != col and abs(row-i) != abs(col-c) for i,c in enumerate(board)):
            solve(board+[col], row+1, N)

N = int(input("Enter board size (default 8): ") or 8)
solve([], 0, N)