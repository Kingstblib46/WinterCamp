from collections import Counter

def solution(n: int, m: int, s: str, c: str) -> int:
    # 统计货架上商品的数量
    shelf_count = Counter(s)
    # 统计顾客需求的商品数量
    customer_count = Counter(c)
    
    # 计算能够满足的需求数量
    total_sold = 0
    for item, need in customer_count.items():
        # 计算该商品能够满足的最大数量
        total_sold += min(shelf_count.get(item, 0), need)
    
    return total_sold

# 测试样例
print(solution(3, 4, "abc", "abcd"))       # 输出 3
print(solution(4, 2, "abbc", "bb"))        # 输出 2
print(solution(5, 4, "bcdea", "abcd"))     # 输出 4
