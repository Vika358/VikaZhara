while True:
    try:
        n = int(input("Введіть кількість розділів (1-20): "))
        if n <= 0:
            print("Кількість розділів має бути від 1 до 20!")
            continue
        if n > 20:
            print("Максимум можна ввести 20 розділів.")
            continue
        break
    except ValueError:
        print("Введіть ціле число, а не текст або дробове значення.")
print("\nОберіть метод сортування:")
print("1 — За зростанням (A → Я)")
print("2 — За спаданням (Я → A)")
print("3 — За довжиною назви")
method = input("Введіть номер методу (1-3): ")
sections = []
for i in range(n):
    name = input(f"Введіть назву розділу {i + 1}: ").strip()
    sections.append(name)
sections = list(set(sections))
if method == "1":
    sections.sort()
elif method == "2":
    sections.sort(reverse=True)
elif method == "3":
    sections.sort(key=len)
else:
    print("Обрано неправильний метод. Використано сортування за замовчуванням (A → Я).")
    sections.sort()
print("Відсортований список розділів:")
for i, title in enumerate(sections, start=1):
    print(f"{i}. {title}")
