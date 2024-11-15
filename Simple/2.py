def solution(s: str) -> str:
    # 分离整数部分和小数部分
    if '.' in s:
        s_int, s_dec = s.split('.', 1)
    else:
        s_int, s_dec = s, ''

    # 去除整数部分的前导零，确保至少有一个零
    s_int = s_int.lstrip('0') or '0'

    # 给整数部分添加千分位逗号
    s_int_with_commas = "{:,}".format(int(s_int))

    # 重新组合整数部分和小数部分
    if s_dec:
        return f"{s_int_with_commas}.{s_dec}"
    else:
        return s_int_with_commas


if __name__ == '__main__':
    print(solution("1294512.12412"))
    print(solution("0000123456789.99"))
    print(solution("987654321"))
