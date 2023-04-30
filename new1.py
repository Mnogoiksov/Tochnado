import csv
from collections import Counter

file_path = "/Users/mnokoiksov/vsyakoe/powerball.csv"

# Read data from the file
data = []
with open(file_path, mode='r', encoding='utf-8') as csvfile:
    tsvreader = csv.reader(csvfile, delimiter='\t')
    for row in tsvreader:
        data.append(row)

# Collect all numbers and Powerballs into lists
all_numbers = []
all_powerballs = []
for row in data:
    all_numbers.extend(row[1:6])
    all_powerballs.append(row[6])

# Find the most common numbers and the most common Powerball
counter_numbers = Counter(all_numbers)
most_common_numbers = counter_numbers.most_common(5)
counter_powerballs = Counter(all_powerballs)
most_common_powerball = counter_powerballs.most_common(1)

# Print the results
print("5 most probable numbers:", [num[0] for num in most_common_numbers])
print("Most probable Powerball:", most_common_powerball[0][0])
