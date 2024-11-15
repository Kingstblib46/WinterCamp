def solution(n: int) -> int:
    matches = 0
    while n > 1:
        if n % 2 == 0:
            matches += n // 2
            n = n // 2
        else:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
    return matches

# 测试样例
if __name__ == '__main__':
    print(solution(7) == 6)    # 输出 6
    print(solution(14) == 13)  # 输出 13
    print(solution(1) == 0)    # 输出 0
