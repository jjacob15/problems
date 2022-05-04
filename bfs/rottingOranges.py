def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = []
    hasFruit = False
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c))
            elif grid[r][c] == 1:
                hasFruit = True

    if len(q) == 0 and not hasFruit:
        return 0

    if len(q) == 0 and hasFruit:
        return -1
    minutes = -1
    while q:
        minutes += 1
        for _ in range(len(q)):
            x, y = q.pop(0)
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != 1:
                    continue      
                grid[nx][ny] = 2
                q.append((nx, ny))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1

    return minutes     


if __name__ == "__main__":
    if orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1:
        print('pass')
    if orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4:
        print('pass')
    if orangesRotting([[0,2]]) == 0:
        print('pass')
    if orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2:
        print('pass')
    if orangesRotting([[[0]]]) == 0:
        print('pass')
