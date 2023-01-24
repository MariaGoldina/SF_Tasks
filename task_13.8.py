N = int(input("Введите количество билетов, которые вы хотите приобрести: "))
cost = 0
for i in range(1, N + 1):
    age = int(input(f"Введите возраст {i}-го посетителя: "))
    if age < 18:
        print("Билет бесплатный")
    elif 18 <= age < 25:
        cost += 990
        print("Цена билета 990 руб.")
    else:
        cost += 1390
        print("Цена балета 1390 руб.")
print("")
discount = 0
if N > 3:
    discount = 10
    total_cost = cost * (1 - discount / 100)
    print("Применена скидка 10% при покупке более 3 билетов.")
else:
    total_cost = cost
print(f"Общая стоимость покупки {N} билета(ов) составляет {total_cost} руб.")