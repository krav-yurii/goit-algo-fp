items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    items_ratio = []
    for item_name, item_info in items.items():
        ratio = item_info['calories'] / item_info['cost']
        items_ratio.append((ratio, item_name, item_info))
    
    items_ratio.sort(reverse=True)
    
    total_cost = 0 
    total_calories = 0
    selected_items = []
    
    for ratio, item_name, item_info in items_ratio:
        if total_cost + item_info['cost'] <= budget:
            total_cost += item_info['cost']
            total_calories += item_info['calories']
            selected_items.append(item_name)
    
    return {
        'selected_items': selected_items,
        'total_cost': total_cost,
        'total_calories': total_calories
    }

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']
        for w in range(budget + 1):
            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    w = budget
    total_cost = 0
    selected_items = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_names[i - 1]
            selected_items.append(item_name)
            item_cost = items[item_name]['cost']
            total_cost += item_cost
            w -= item_cost
    
    total_calories = dp[n][budget]
    selected_items.reverse() 
    
    return {
        'selected_items': selected_items,
        'total_cost': total_cost,
        'total_calories': total_calories
    }

def main():
    budget = int(input("Введіть ваш бюджет: "))
    
    print("\nЖадібний алгоритм:")
    greedy_result = greedy_algorithm(items, budget)
    print(f"Вибрані страви: {greedy_result['selected_items']}")
    print(f"Загальна вартість: {greedy_result['total_cost']}")
    print(f"Загальна калорійність: {greedy_result['total_calories']}")
    
    print("\nАлгоритм динамічного програмування:")
    dp_result = dynamic_programming(items, budget)
    print(f"Вибрані страви: {dp_result['selected_items']}")
    print(f"Загальна вартість: {dp_result['total_cost']}")
    print(f"Загальна калорійність: {dp_result['total_calories']}")

if __name__ == "__main__":
    main()