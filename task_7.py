import random
import matplotlib.pyplot as plt

def simulate_dice_throws(throws):
    sum_counts = {i: 0 for i in range(2, 13)}

    # Імітація кидків
    for _ in range(throws):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1

    # Обчислення ймовірностей
    probabilities = {sum_: count / throws for sum_, count in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    # Побудова графіка
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума двох кубиків')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

# Кількість кидків
throws = 1000000
probabilities = simulate_dice_throws(throws)

# Вивід таблиці ймовірностей
print("Сума | Ймовірність")
for sum_, prob in probabilities.items():
    print(f"{sum_:4} | {prob:.2%}")

# Візуалізація результатів
plot_probabilities(probabilities)