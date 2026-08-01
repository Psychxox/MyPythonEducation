doubled_numbers = [4, 7, 4, 2, 9, 7, 4, 1, 9]
unique = []

for i in doubled_numbers:
    if i not in unique:
        unique += [i]

print(doubled_numbers)
print(unique)

numbers = [4, 7, 4, 2, 9, 7, 4, 1, 9]
unique = []

for num in numbers:
    # Проверяем вручную: есть ли num в unique?
    found = False
    for u in unique:
        if u == num:
            found = True
            break
    
    if not found:
        unique += [num]

print(f"\nБез дубликатов: {unique}")