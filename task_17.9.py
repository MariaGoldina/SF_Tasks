try:
    num_list = list(map(int, input("Введите последовательность целых чисел через пробел ").split()))
except ValueError as e:
    num_list = list(map(int, input("Неверный ввод. Введите последовательность ЦЕЛЫХ ЧИСЕЛ через пробел ").split()))


def sort_list():
    for i in range(1, len(num_list)):
        x = num_list[i]
        idx = i
        while idx > 0 and num_list[idx-1] > x:
            num_list[idx] = num_list[idx-1]
            idx -= 1
        num_list[idx] = x


sort_list()
print(f"Введенная последовательность после сортировки по возрастанию имеет вид: {num_list}")


def binary_search_list(list_, element, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if list_[middle] < element <= list_[middle + 1]:
        return middle
    elif element < list_[middle]:
        return binary_search_list(list_, element, left, middle-1)
    else:
        return binary_search_list(list_, element, middle+1, right)


try:
    num = int(input("Введите любое целое число "))
except ValueError as e:
    num = int(input("Неверный ввод. Введите любое ЦЕЛОЕ ЧИСЛО "))

if num not in num_list and num < num_list[0]:
    print("Введенное число не входит в последовательность."
          "\nЭлемента последовательности меньше введенного числа не существует.")
elif num not in num_list and num > num_list[len(num_list)-1]:
    print("Введенное число не входит в последовательность."
          f"\nЭлемент последовательности меньше введенного числа имеет индекс {len(num_list)-1}, "
          f"элементов больше введенного числа не существует")
else:
    if num_list.count(num) > 1 and num_list[0] != num:
        for i, a in enumerate(num_list):
            if a < num and num_list[i+1] == num:
                print(f"Элемент последовательности меньше введенного числа имеет индекс {i}.")
    elif num_list[0] == num:
        print("Элемента последовательности меньше введенного числа не существует.")
    else:
        print(f"Элемент последовательности меньше введенного числа имеет индекс "
              f"{binary_search_list(num_list, num, 0, (len(num_list)-1))}.")
