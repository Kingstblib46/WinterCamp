def solution(n: int, k: int) -> int:
    # 根据公式计算数组元素的最小和
    return k * n * (n + 1) // 2

# 测试样例
print(solution(3, 1))  # 输出 6
print(solution(2, 2))  # 输出 6
print(solution(4, 3))  # 输出 30
