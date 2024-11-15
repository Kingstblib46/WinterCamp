def solution(numbers):
    """
    计算从每个组中选择一个数字，使得所有选中数字的和为偶数的组合数量。

    参数:
        numbers (List[int]): 一个由整数构成的列表，每个整数代表一个数字组（数字从'1'到'9'）。

    返回:
        int: 满足条件的选择方法总数。
    """
    # 初始化偶数和组合数为1，奇数和组合数为0
    even_count = 1
    odd_count = 0

    for group in numbers:
        # 将组的整数转换为数字列表
        digits = [int(d) for d in str(group)]
        
        # 计算当前组中偶数和奇数的数量
        group_even = sum(1 for d in digits if d % 2 == 0)
        group_odd = len(digits) - group_even

        # 更新组合计数
        new_even = even_count * group_even + odd_count * group_odd
        new_odd = even_count * group_odd + odd_count * group_even

        even_count, odd_count = new_even, new_odd

    return even_count

if __name__ == "__main__":
    # 你可以在这里添加更多测试用例
    print(solution([123, 456, 789]))
    print(solution([123456789]))
    print(solution([14329, 7568]))