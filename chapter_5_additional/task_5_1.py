numbers = [10, 20, 30, 40, 50, 60, 70]
result = ""

for i in range(0, len(numbers), 2):
    if result:
        result += ", "
    result += str(numbers[i])

print(result)  # 10, 30, 50, 70