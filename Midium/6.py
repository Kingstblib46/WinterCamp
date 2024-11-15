def solution(m: int, n: int, a: list) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
    max_path = 0  # 最大移动次数

    def dfs(x, y, prev_val, direction, length, visited):
        nonlocal max_path
        max_path = max(max_path, length)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if (direction == "up" and a[nx][ny] > prev_val) or (direction == "down" and a[nx][ny] < prev_val):
                    visited.add((nx, ny))
                    dfs(nx, ny, a[nx][ny], "down" if direction == "up" else "up", length + 1, visited)
                    visited.remove((nx, ny))

    # 从每个位置开始进行 DFS
    for i in range(m):
        for j in range(n):
            dfs(i, j, a[i][j], "up", 1, {(i, j)})  # 先尝试上坡
            dfs(i, j, a[i][j], "down", 1, {(i, j)})  # 再尝试下坡

    return max_path - 1

# 测试样例
print(solution(2, 2, [[1, 2], [4, 3]]))  # 输出 3
print(solution(3, 3, [[10, 1, 6], [5, 9, 3], [7, 2, 4]]))  # 输出 8
print(solution(4, 4, [[8, 3, 2, 1], [4, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]))  # 输出 11
