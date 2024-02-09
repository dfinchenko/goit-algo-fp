def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item in sorted_items:
        item_name = item[0]
        item_cost = item[1]["cost"]
        item_calories = item[1]["calories"]

        if total_cost + item_cost <= budget:
            selected_items.append(item_name)
            total_cost += item_cost
            total_calories += item_calories

    return selected_items, total_calories

def dynamic_programming(items, budget):
    items_list = list(items.items())
    n = len(items_list)
    dp = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            item_cost = items_list[i-1][1]["cost"]
            item_calories = items_list[i-1][1]["calories"]
            if item_cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-item_cost] + item_calories)
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items_list[i-1][0])
            w -= items_list[i-1][1]["cost"]

    selected_items.reverse()
    total_calories = dp[n][budget]

    return selected_items, total_calories

# Дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
# Виклик функції жадібного алгоритму
print("\nРезультат жадібного алгоритму:", selected_items_greedy, "з загальною кількістью калорій:", total_calories_greedy)

# Виклик функції динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nРезультат динамічного програмування:", selected_items_dp, "з загальною кількістью калорій:", total_calories_dp)
