per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
rates=per_cent.values()

money=float(input("Введите сумму вклада: "))

deposit_income=[x/100*money for x in rates]
print(deposit_income)
Max_income=max(deposit_income)
print("Максимальная сумма, которую вы можете заработать — ", Max_income)