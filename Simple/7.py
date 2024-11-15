def solution(a: int, b: int) -> int:
    # 计算最少需要的天数，使用整数向上取整的方法
    return (a + b - 1) // b

if __name__ == '__main__':
    print(solution(10, 1) == 10)
    print(solution(10, 2) == 5)
    print(solution(10, 3) == 4)
