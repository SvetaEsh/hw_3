stroka="Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

# Count number of characters.
print("1. количество символов:", len(stroka))

# Expand row. Python yes -> sey nohtyP
print("2. Развернутая строка:", stroka[::-1])

# Capitalize every word
print("3. Предложение, в котором каждое слово с большой буквы:", stroka.title())

# Make all text capitalize
print("4. весь текст прописными буквами:", stroka.lower())

# Find the number of occurrences "нд", "ам", "о" in a string
print("5а. Найти число вхождений 'нд':", stroka.count("нд"))
print("5б. Найти число вхождений 'ам':", stroka.count("ам"))
print("5в. Найти число вхождений 'о':", stroka.count("о"))

# Own exercises
print("Номер индекса буквы'з' со среза:",stroka.find("з", 1,10))
print("Заменить Лондон на Москву:", stroka.replace("Лондоне", "Москве"))
print("Создать список и обьединить его в строку:",' '.join(stroka.split()))
print("Удалить начало строки:", stroka.lstrip("Не знаю, как там в Лондоне, я не была. "))

#Print the original string to the console
print(stroka)

# Expand offer. Я Денис -> Денис Я
stroka="Я Денис"
list=stroka.split()
list.reverse()
print(' '.join(list))

#Print the original string to the console
print(stroka)