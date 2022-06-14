# #Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран
# Пример работы: Введите количество элементов: 3
# Введите 1 элемент: 5
# Введите 2 элемент: 2
# Введите 3 элемент: 4
# Вывод: [2, 4, 5]

num_lis_elements = int(input('Введите количество элементов списка: '))
user_numbers = []
element_number = 1

while len(user_numbers) < num_lis_elements:
    user_numbers.append(int(input(f'Введите {element_number} число: ')))
    element_number = element_number + 1

user_numbers.sort()
print(user_numbers)
