def getMaximumGold(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        gold = grid[x][y]
        grid[x][y] = 0
        max_gold = 0
        for dx, dy in directions:
            max_gold = max(max_gold, dfs(x + dx, y + dy))
        
        grid[x][y] = gold

        return max_gold + gold

    max_total_gold = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                max_total_gold = max(max_total_gold, dfs(i, j))
    
    return max_total_gold


def input_grid():
    n, m = map(int, input().split())  
    
    grid = []

    for _ in range(n):
        row = list(map(int, input().split()))  
        grid.append(row)
    
    return grid

if __name__ == "__main__":
    grid = input_grid()  
    result = getMaximumGold(grid)
    print(result) 
