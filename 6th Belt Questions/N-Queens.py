n = int(input())

solutions = []
cols = set()  
diag1 = set()  
diag2 = set()  
board = [['.'] * n for _ in range(n)]  

def backtrack(row):
    if row == n:
        solution = ["".join(board[i]) for i in range(n)]
        solutions.append(solution)
        return
    
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        
        board[row][col] = 'Q'
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        
        backtrack(row + 1)
        
        board[row][col] = '.'
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

backtrack(0)

solutions.sort()

for solution in solutions:
    for row in solution:
        print(row)
    print() 
