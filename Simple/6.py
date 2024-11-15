def solution(array):
    candidate = None
    count = 0
    
    # 第一遍遍历，找出候选数
    for num in array:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    # 第二遍遍历，确认候选数是否为多数元素
    if array.count(candidate) > len(array) // 2:
        return candidate
    else:
        return None

# 测试样例
print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]))  # 输出 3
print(solution([5, 5, 5, 1, 2, 5, 5]))        # 输出 5
print(solution([9, 9, 9, 9, 8, 9, 8, 8]))     # 输出 9