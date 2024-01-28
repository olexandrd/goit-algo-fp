from constants import items


def greedy_algorithm(items: dict, max_cost: int):
    """
    Greedy algorithm that returns the best combination of items
    based on the calories/cost ratio of the items.
    """
    # Sort the items by calories/cost ratio
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"])
    # Initialize the result
    result = []
    # Iterate over the sorted items
    for item in sorted_items:
        # Check if the cost of the item is less than the max_cost
        if item[1]["cost"] <= max_cost:
            # Add the item to the result
            result.append(item[0])
            # Subtract the cost of the item from the max_cost
            max_cost -= item[1]["cost"]
    # Return the result
    return result


def dynamic_programming_algorithm(items: dict, max_cost: int):
    """
    Dynamic programming algorithm that returns the best combination of items
    based on the calories/cost ratio of the items.
    """
    # Initialize the result
    result = []
    # Initialize the table
    table = [[0 for _ in range(max_cost + 1)] for _ in range(len(items) + 1)]
    # Iterate over the items
    for i in range(1, len(items) + 1):
        # Iterate over the max_cost
        for j in range(1, max_cost + 1):
            # Check if the cost of the item is less than the max_cost
            if items[list(items.keys())[i - 1]]["cost"] <= j:
                # Get the maximum value between the previous item and the current item
                table[i][j] = max(
                    table[i - 1][j],
                    table[i - 1][j - items[list(items.keys())[i - 1]]["cost"]]
                    + items[list(items.keys())[i - 1]]["calories"],
                )
            else:
                # Get the previous item
                table[i][j] = table[i - 1][j]
    # Get the maximum value from the table
    max_value = table[-1][-1]
    # Get the index of the maximum value
    index = table[-1].index(max_value)
    # Iterate over the table
    for i in range(len(table) - 1, 0, -1):
        # Check if the maximum value is not equal to the previous value
        if max_value != table[i - 1][index]:
            # Add the item to the result
            result.append(list(items.keys())[i - 1])
            # Subtract the cost of the item from the max_cost
            max_value -= items[list(items.keys())[i - 1]]["calories"]
            # Subtract the index of the item from the index
            index -= items[list(items.keys())[i - 1]]["cost"]
    # Return the result
    return result


def main():
    max_cost = 100
    greedy_result = greedy_algorithm(items, max_cost)
    dynamic_programming_result = dynamic_programming_algorithm(items, max_cost)
    # Print the results
    print("Greedy algorithm result:", greedy_result)
    print("Dynamic programming algorithm result:", dynamic_programming_result)


if __name__ == "__main__":
    main()
