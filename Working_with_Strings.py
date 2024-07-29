# Задача 3.1

# Дана следующая строка: ‘Сидел барсук в своей норе и ел картошечку пюре’

# 1. Создайте данную строку
# 2. Получите ее длину
# 3. Проведите операцию сложения со строкой ‘.’
# 4. Проверьте, входит ли подстрока ‘ре’ в заданную строку
# 5. Посчитайте количество вхождений подстроки ‘ре’
# 6. Получите предпоследний символ строки
# 7. Получите все символы с нечетными индексами
# 8. Определите, сколько слов в строке


# 1. Создаем строку
>>> my_str = 'Сидел барсук в своей норе и ел картошечку пюре'

# 2. Получаем длину строки с помощью встроенного метода len()
>>> len(my_str)
46

# 3. Выполняем конкатенацию строк
>>> my_str + '.'
'Сидел барсук в своей норе и ел картошечку пюре.'

# 4. Определяем вхождение подстроки 'ре'
>>> 'ре' in my_str
True

# 5. Определяем количество вхождений подстроки 'ре'
>>> my_str.count('ре')
2

# 6. Получаем предпоследний символ строки
>>> my_str[-2]
'р'

# 7. Получаем элементы с нечетными индексами
# Для этого выполняем срез, начиная с элемента с индексом 1 по конец строки с шагом 2
>>> my_str[1::2]
'ие асквсойнр  лкроек юе'

# 8. Определяем количество слов в строке
# Для этого считаем количество пробелов и прибавляем 1
>>> my_str.count(' ') + 1
9


# 3.2
# ана строка: ‘пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.’

# 1. Начните строку с заглавной буквы, если она находится в нижнем регистре.
# 2. Найдите индекс вхождения подстроки ‘сопровождать’.
# 3. Замените вхождение подстроки ‘сопровождать’ на ‘поддерживать’.
# 4. Разбейте предложение на части по запятым. Соедините части обратно, снова добавив запятые между частями.

# 1. Создаем строку
>>> my_str = 'пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'

# 2. Проверяем регистр строки и делаем первую букву заглавной, если регистр нижний
>>> if my_str.islower(): my_str.capitalize()
... 
'Пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'

# 3. Ищем индекс вхождения подстроки 'сопровождать'
# Вариант 1: Используем метод find() - строковый метод
>>> my_str.find('сопровождать')
26
# Вариант 2: Используем метод index() - метод для работы с любыми последовательностями
>>> my_str.index('сопровождать')
26

# 4. Заменяем подстроку 'сопровождать' на 'поддерживать'
>>> my_str.replace('сопровождать', 'поддерживать')
'пишите код так, как будто поддерживать его будет склонный к насилию психопат, который знает, где вы живете.'

# 5. Разбиваем строку на подстроки по разделителю ',' и сохраняем подстроки в список
>>> lst = my_str.split(',')
>>> lst
['пишите код так', ' как будто сопровождать его будет склонный к насилию психопат', ' который знает', ' где вы живете.']

# Соединяем полученные ранее подстроки обратно
>>> ','.join(lst)
'пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'


# Задача 3.3

# Дано имя файла. Необходимо вывести его расширение.

# Импортируем стандартный модуль re для работы с регулярными выражениями
import re

# Создаем константу для имени файла, которое будет использовать для тестов
FILENAME = 'folder1/folder2/file.ext'


# Вариант решения 1 - пользуемся срезами
def extention_slice(filename):
    # Находим индекс точки
    point_pos = filename.find('.')
    # Возвращаем срез начиная с позиции после точки и до конца имени файла
    return filename[point_pos + 1:]


# Вариант решения 2 - используем функцию partition()
def extention_part(filename):
    # С помощью метода partition() разбиваем имя файла на 3 части
    # В качестве разделителя используем символ '.'
    # Метод partition() возвращает кортеж из 3 элеметов
    # Возвращаем 3-й элемент
    return filename.partition('.')[2]


# Вариант решения 3 - пользуемся регулярными выражениями
def extention_regex(filename):
    # Формируем регулярное выражение для поиска расширения:
    # \. - ищем символ точки в строке
    # .+$ - после точки ищем любые символы вплоть до конца строки
    # (.+$) - скобками формируем группу(это необходимо, чтобы получить не точку с расширением, а только само расширение)
    regex = r'\.(.+$)'
    # Обращаемся к модулю re и вызываем для него метод search для поиска подстроки по регулярному выражению
    # Из результата берем группу с индексом 1 
    # Это часть подстроки, которая подходит под выражение в скобках (например, 'ext')
    # Группа с индексом 0 - это полная подстрока, подходящая под регулярное выражение(например, '.ext')
    return re.search(regex, filename)[1]


# Тесты
if __name__ == '__main__':
    print(extention_slice(FILENAME))
    print(extention_part(FILENAME))
    print(extention_regex(FILENAME))
