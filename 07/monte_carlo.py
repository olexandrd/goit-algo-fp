import networkx as nx
import matplotlib.pyplot as plt
import random


def roll_dice(dices: int):
    return sum(random.randint(1, 6) for _ in range(dices))


def dice_result(rolls: int) -> dict:
    dice_result = {i: 0 for i in range(2, 13)}

    for roll in range(rolls):
        dice_result[roll_dice(2)] += 1

    dice_result_occurrence = {
        sum: occurrences / rolls for sum, occurrences in dice_result.items()
    }
    return dice_result, dice_result_occurrence


def print_markdown_table(data: dict):
    print("| Sum | Occurrence |")
    print("| --- | ---------- |")
    for sum, occurrence in data.items():
        print(f"| {sum} | {occurrence * 100:.2f}% |")


# Roll the dice 10000 times
_, dice_result_occurrence = dice_result(10000)
print_markdown_table(dice_result_occurrence)


def draw_plot(occurrence: dict, name: str = "Dice result occurrence"):
    occurrence = {key: value * 100 for key, value in occurrence.items()}
    plt.bar(occurrence.keys(), occurrence.values())
    plt.title(name)
    plt.ylabel("Occurrence, %")
    plt.xlabel("Dice sum")
    plt.show()


draw_plot(dice_result_occurrence)
