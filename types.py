# Задача 1.1

# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка


# 1. Создаем список
lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 2. Добавляем элемент с типом str в конец списка
lst.append('Строка')
#[1, 1, 1, 1, 1, 1, 1, 1, 1, 'Строка']

# 3. Вставляем элемент со значением 189 на место с индексом 4
lst[4] = 189
# Результат: [1, 1, 1, 1, 189, 1, 1, 1, 1, 1, 'Строка']

# 4. Добавляем вложенный список ['a', 'b', 'a', 'hello']
lst.append(['a', 'b', 'a', 'hello'])
# Результат: [1, 1, 1, 1, 189, 1, 1, 1, 1, 1, 'Строка', ['a', 'b', 'a', 'hello']]

# 5. Вставляем кортеж со значением (1, 6, 89) на место с индексом -3 (3-й элемент с конца списка)
lst[-3] = (1, 6, 89)
# Результат: [1, 1, 1, 1, 189, 1, 1, 1, 1, (1, 6, 89), 'Строка', ['a', 'b', 'a', 'hello']]

# 6. Получаем значение элемента с индексом 0
lst[0]
# 1
# Получаем значение элемента с индексом -1(последний элемент списка)
 lst[-1]
# ['a', 'b', 'a', 'hello']

# 7. Удаляем элемент со значением 189
lst.remove(189)
# Результат: [1, 1, 1, 1, 1, 1, 1, 1, (1, 6, 89), 'Строка', ['a', 'b', 'a', 'hello']]

# 8. Считаем количество элементов в списке со значением 1
lst.count(1)
8


# Задача 1.2

# Получите первый и последний элемент списка

lst = ['Нулевой элемент', 'One', 2, 3, 4, (5, 5, 5)]
lst[0]
# 'Нулевой элемент'
lst[-1]
# (5, 5, 5)


# Задача 1.3

# Поменяйте значения переменных a и b местами

a = 100
b = 'Строка'
a, b = b, a
print(a)
# 'Строка'
print(b)
# 100
