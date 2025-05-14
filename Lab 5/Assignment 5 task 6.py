from collections import deque
R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[0]*H for _ in range(R)]
max_diamonds = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            q = []
            q.append((i, j))
            visited[i][j] = 1
            diamonds = 1 if grid[i][j] == 'D' else 0

            while q:
                x, y = q.pop(0)
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < R and 0 <= ny < H:
                        if not visited[nx][ny] and grid[nx][ny] != '#':
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                            if grid[nx][ny] == 'D':
                                diamonds += 1
            max_diamonds = max(max_diamonds, diamonds)

print(max_diamonds)
