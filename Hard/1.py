def solution(n: int, k: int, s: str) -> str:
    s = list(s)  # 将字符串转换为列表，便于操作字符
    for i in range(n):
        if s[i] == '0':
            # 尝试将当前的 '0' 向左移动
            j = i
            while j > 0 and s[j - 1] == '1' and k > 0:
                # 交换相邻的 '0' 和 '1'
                s[j], s[j - 1] = s[j - 1], s[j]
                j -= 1
                k -= 1  # 每次交换，减少一次操作次数
                if k == 0:  # 用尽所有操作次数
                    return ''.join(s)
    return ''.join(s)

# 测试用例
print(solution(5, 2, "01010"))   # 输出应为 '00101'
print(solution(7, 3, "1101001")) # 输出应为 '0110101'
print(solution(4, 1, "1001"))    # 输出应为 '0101'
