import random
import matplotlib.pyplot as plt
import pandas as pd

theoretical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)} 
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2     
        sums_count[dice_sum] += 1  
    
    probabilities = {sum_value: count / num_rolls for sum_value, count in sums_count.items()}
    
    return probabilities

def main():
    num_rolls = int(input("Введіть кількість кидків для симуляції (рекомендується 10,000 або більше): "))
    
    simulated_probabilities = simulate_dice_rolls(num_rolls)
    
    sums = list(range(2, 13))
    sim_probs = [simulated_probabilities[sum_value] * 100 for sum_value in sums]  
    theor_probs = [theoretical_probabilities[sum_value] * 100 for sum_value in sums] 
    
    data = {
        "Сума": sums,
        "Симуляційна ймовірність (%)": sim_probs,
        "Теоретична ймовірність (%)": theor_probs
    }
    df = pd.DataFrame(data)
    print("\nТаблиця ймовірностей:")
    print(df)
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_probs, width=0.4, label='Симуляція', color='skyblue', align='edge')
    plt.bar([s - 0.4 for s in sums], theor_probs, width=0.4, label='Теорія', color='orange', align='edge')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
