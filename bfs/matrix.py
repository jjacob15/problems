'''
This one is hard. You need to set all non zero cells to -1 and then bfs the zero cells.
if 
''' 
from collections import deque

def matrix(mat):
    m, n = len(mat), len(mat[0])

    q = deque([])
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                continue
            mat[nr][nc] = mat[r][c] + 1

            q.append((nr, nc))
    return mat


if __name__ == "__main__":
    # matrix([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]])
    if matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]:
        print('pass')
    # if matrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]) == [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]:
    #     print('pass')
