MOD = 10**9 + 7

def solution(n: int, a: list, b: list) -> int:
    # 初始化 DP 数组
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1  # 初始状态：空集的方案数

    # 动态规划更新 DP 数组
    for i in range(1, n + 1):
        for j in range(3):
            # 选择正面 a[i-1] 的情况
            dp[i][(j + a[i - 1]) % 3] = (dp[i][(j + a[i - 1]) % 3] + dp[i - 1][j]) % MOD
            # 选择背面 b[i-1] 的情况
            dp[i][(j + b[i - 1]) % 3] = (dp[i][(j + b[i - 1]) % 3] + dp[i - 1][j]) % MOD

    # 返回使得和模 3 等于 0 的方案数
    return dp[n][0]

# 测试样例
print(solution(3, [1, 2, 3], [2, 3, 2]))   # 输出应为 3
print(solution(4, [3, 1, 2, 4], [1, 2, 3, 1]))  # 输出应为 6
print(solution(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # 输出应为 32
