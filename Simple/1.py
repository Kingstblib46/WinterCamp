def solution(cards):
    result = 0
    for num in cards:
        result ^= num
    return result

if __name__ == "__main__":
    # 测试样例
    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]))  # 输出：4
    print(solution([0, 1, 0, 1, 2]))              # 输出：2
    print(solution([7, 3, 3, 7, 10]))             # 输出：10
