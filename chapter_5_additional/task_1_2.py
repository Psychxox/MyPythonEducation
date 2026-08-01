total = 0

for i in range(50):
    i += 1
    if i % 2 == 0:
        total += i
print(f"Сумма всех чётных чисел 1 - 50: {total}")