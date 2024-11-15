def solution(n, array):
    max_area = 0
    
    # 遍历每个可能的起点
    for i in range(n):
        min_height = float('inf')  # 初始化最小高度
        # 尝试不同的子数组长度 k，从 1 到 n-i
        for k in range(1, n - i + 1):
            # 更新当前子数组的最小高度
            min_height = min(min_height, array[i + k - 1])
            # 计算当前子数组的面积
            area = k * min_height
            # 更新最大面积
            max_area = max(max_area, area)
    
    return max_area

# 测试样例
print(solution(5, [1, 2, 3, 4, 5]))  # 输出 9
print(solution(6, [5, 4, 3, 2, 1, 6]))  # 输出 9
print(solution(4, [4, 4, 4, 4]))  # 输出 16
