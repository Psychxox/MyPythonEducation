result = ""

for i in range(20, 0, -1):
    if result:
        result += " "
    result += str(i)
print(f"Обратный порядок: {result}")