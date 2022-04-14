from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows = len(image)
    cols = len(image[0])
    visited = [[0 for c in range(cols)] for r in range(rows)]
    match = image[sr][sc]

    def dfs(image: List[List[int]], row: int, col: int, visited: List[List[int]], newColor: int, match: int):
        if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0 or visited[row][col] == 1 or image[row][col] != match:
           return

        visited[row][col] = 1
        image[row][col] = newColor

        dfs(image, row - 1, col, visited, newColor, match)
        dfs(image, row, col - 1, visited, newColor, match)
        dfs(image, row, col + 1, visited, newColor, match)
        dfs(image, row + 1, col, visited, newColor, match)

    dfs(image, sr, sc, visited, newColor, match)

    return image


if __name__ == "__main__":
    if floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) != [[2, 2, 2], [2, 2, 0], [2, 0, 1]]:
        print('fail')
    if floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2) != [[2, 2, 2], [2, 2, 2]]:
        print('fail')
