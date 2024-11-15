import re

def solution(n, template, titles):
    # 将模板中的通配符 {} 替换为正则表达式的 .*，表示可以匹配任意字符
    regex_pattern = re.sub(r'\{.*?\}', '.*', template)
    regex_pattern = f"^{regex_pattern}$"  # 确保整个字符串匹配

    result = []
    # 对每个标题进行匹配
    for title in titles:
        # 检查标题是否匹配正则表达式
        if re.match(regex_pattern, title):
            result.append("True")
        else:
            result.append("False")

    # 返回以逗号分隔的结果字符串
    return ",".join(result)

# 测试用例
if __name__ == "__main__":
    print(solution(4, "ad{xyz}cdc{y}f{x}e", ["adcdcefdfeffe", "adcdcefdfeff", "dcdcefdfeffe", "adcdcfe"]))  # "True,False,False,True"
    print(solution(3, "a{bdc}efg", ["abcdefg", "abefg", "efg"]))  # "True,True,False"
    print(solution(5, "{abc}xyz{def}", ["xyzdef", "abcdef", "abxyzdef", "xyz", "abxyz"]))  # "True,False,True,True,True"
