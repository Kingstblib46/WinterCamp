def solution(n, max_val, array):
    """
    在一场经典的德州扑克游戏中，找到符合条件的最大的“葫芦”组合。

    参数:
        n (int): 总牌数。
        max_val (int): “葫芦”组成的五张牌牌面值之和的最大值。
        array (List[int]): 一组牌的牌面值列表。

    返回:
        List[int]: 包含三张相同牌面值和两张相同牌面值的列表。如果找不到符合条件的“葫芦”，返回 [0, 0]。
    """
    from collections import Counter

    # 牌面值的优先级顺序：A（1） > K（13） > Q（12） > J（11） > 10 > 9 > ... > 2
    card_rank = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # 创建牌面值到优先级的映射
    rank_map = {card: idx for idx, card in enumerate(card_rank)}

    # 统计每个牌面值的数量
    counts = Counter(array)
    
    # 筛选出所有可以作为“三条”的牌面值，并按优先级排序（高到低）
    triplet_candidates = sorted(
        [card for card, cnt in counts.items() if cnt >= 3],
        key=lambda x: rank_map.get(x, len(card_rank)),
    )

    for a in triplet_candidates:
        # 筛选出所有可以作为“对子”的牌面值，且不等于a，并按优先级排序（高到低）
        pair_candidates = sorted(
            [card for card, cnt in counts.items() if cnt >=2 and card != a],
            key=lambda x: rank_map.get(x, len(card_rank)),
        )
        for b in pair_candidates:
            total = 3 * a + 2 * b
            if total <= max_val:
                return [a, b]
    
    return [0, 0]

if __name__ == "__main__":
    # 添加测试样例
    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]))        # 输出: [8, 5]
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]))       # 输出: [6, 13]
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]))   # 输出: [0, 0]
    # 错误样例
    print(solution(31, 42, [3,3,11,12,12,2,13,5,13,1,13,8,8,1,8,13,12,9,2,11,3,5,8,11,1,11,1,5,4,2,5]))  # 输出: [1, 13]