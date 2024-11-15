def solution(values):
    max_score = 0
    max_i_plus_i = values[0] + 0  # 初始的 values[i] + i
    
    # 从第二个元素开始遍历
    for j in range(1, len(values)):
        # 计算得分：max_i_plus_i + values[j] - j
        max_score = max(max_score, max_i_plus_i + values[j] - j)
        
        # 更新 max_i_plus_i，尝试加入新的 values[j] + j
        max_i_plus_i = max(max_i_plus_i, values[j] + j)
    
    return max_score

# 测试样例
print(solution([8, 3, 5, 5, 6]))   # 输出 11
print(solution([10, 4, 8, 7]))     # 输出 16
print(solution([1, 2, 3, 4, 5]))   # 输出 8
