import csv
from collections import Counter

file_path = "/Users/mnokoiksov/vsyakoe/powerball.csv"

# Считываем данные из файла
data = []
with open(file_path, mode='r', encoding='utf-8') as csvfile:
    tsvreader = csv.reader(csvfile, delimiter='\t')
    for row in tsvreader:
        data.append(row)

# Собираем все числа и Powerball в списки
all_numbers = []
all_powerballs = []
for row in data:
    all_numbers.extend(row[1:6])
    all_powerballs.append(row[6])

# Находим 5 самых часто встречающихся чисел и самый часто встречающийся Powerball
counter_numbers = Counter(all_numbers)
most_common_numbers = counter_numbers.most_common(5)
counter_powerballs = Counter(all_powerballs)
most_common_powerball = counter_powerballs.most_common(1)

# Выводим результаты
print("5 самых часто выпадающих чисел:", [num[0] for num in most_common_numbers])
print("Самый часто выпадающий Powerball:", most_common_powerball[0][0])

# Считаем, сколько раз каждый обычный шар и Powerball выпал
sorted_numbers = sorted(counter_numbers.items(), key=lambda x: x[1], reverse=True)
sorted_powerballs = sorted(counter_powerballs.items(), key=lambda x: x[1], reverse=True)

# Выводим результаты
print("\nКоличество выпадений обычных шаров в порядке убывания:")
for number, count in sorted_numbers:
    print(f"Шар {number} выпал {count} раз(а)")

print("\nКоличество выпадений Powerball в порядке убывания:")
for number, count in sorted_powerballs:
    print(f"Powerball {number} выпал {count} раз(а)")
