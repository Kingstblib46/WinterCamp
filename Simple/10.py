def solution(dna1: str, dna2: str) -> int:
    m, n = len(dna1), len(dna2)
    # 创建dp数组并初始化
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化边界条件
    for i in range(m + 1):
        dp[i][0] = i  # 删除操作
    for j in range(n + 1):
        dp[0][j] = j  # 插入操作
    
    # 填充dp数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1,  # 替换
                               dp[i][j - 1] + 1,      # 插入
                               dp[i - 1][j] + 1)      # 删除
    
    return dp[m][n]

# 测试样例
print(solution("AGT", "AGCT"))       # 输出 1
print(solution("AACCGGTT", "AACCTTGG"))  # 输出 4
print(solution("ACGT", "TGC"))       # 输出 3
print(solution("A", "T"))            # 输出 1
print(solution("GGGG", "TTTT"))      # 输出 4
