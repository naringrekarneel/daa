n = int(input("Enter number of items: "))
weights = list(map(float, input("Enter weights: ").split()))
values = list(map(float, input("Enter values: ").split()))
capacity = float(input("Enter knapsack capacity: "))

ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
ratio.sort(reverse=True)  # sort by value/weight ratio

total_value = 0
for r, w, v in ratio:
    if capacity >= w:
        total_value += v
        capacity -= w
    else:
        total_value += r * capacity
        break

print("Maximum value in knapsack =", round(total_value, 2))
