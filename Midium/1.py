def solution(n: int, k: int, data: list) -> int:
    """
    Calculate the minimum cost for small R to complete the hiking trip.

    Args:
        n (int): Total number of days.
        k (int): Maximum number of food units that can be carried.
        data (List[int]): List containing the price of food at each day's supply station.

    Returns:
        int: The minimum total cost.
    """
    min_total_cost = 0
    current_food = 0

    for i in range(n):
        # Find the next day with a cheaper price
        next_cheaper_day = -1
        for j in range(i + 1, n):
            if data[j] < data[i]:
                next_cheaper_day = j
                break
        
        # Determine how many days we need to buy food for
        if next_cheaper_day == -1:
            days_to_buy = n - i
        else:
            days_to_buy = next_cheaper_day - i
        
        # Calculate the required amount to buy
        required = days_to_buy
        buy = min(required - current_food, k - current_food)
        buy = max(buy, 0)
        
        min_total_cost += buy * data[i]
        current_food += buy
        # Consume one unit for today
        current_food -= 1

    return min_total_cost

if __name__ == "__main__":
    # Test Case 1
    print(solution(5, 2, [1, 2, 3, 3, 2]))  # Expected Output: 9

    # Test Case 2
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]))  # Expected Output: 9

    # Test Case 3
    print(solution(4, 1, [3, 2, 4, 1]))  # Expected Output: 10
