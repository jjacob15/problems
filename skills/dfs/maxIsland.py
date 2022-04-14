from typing import List

def maxIsland(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    maxlength = 0

    def dfs(image: List[List[int]], row: int, col: int, visited: List[List[int]], length: List):
        if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0 or visited[row][col] == 1 or image[row][col] != 1:
           return

        visited[row][col] = 1
        length.append(1)

        dfs(image, row - 1, col, visited,length)
        dfs(image, row, col - 1, visited,length)
        dfs(image, row, col + 1, visited,length)
        dfs(image, row + 1, col, visited, length)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and visited[r][c] == 0:
                length = []
                dfs(grid, r, c, visited, length)
                maxlength = max(maxlength, len(length))

    return maxlength


if __name__ == "__main__":
    if maxIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) != 6:
        print('fail')
    if maxIsland([[0,0,0,0,0,0,0,0]]) != 0:
        print('fail')
