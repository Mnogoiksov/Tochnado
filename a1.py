import csv
import random
from collections import Counter
import tkinter as tk
from tkinter import filedialog, Toplevel


def analyze_most_common(all_numbers, all_powerballs):
    counter_numbers = Counter(all_numbers)
    most_common_numbers = counter_numbers.most_common(5)
    counter_powerballs = Counter(all_powerballs)
    most_common_powerball = counter_powerballs.most_common(1)

    return f"5 самых часто выпадающих чисел: {', '.join(num[0] for num in most_common_numbers)}\nСамый часто выпадающий Powerball: {most_common_powerball[0][0]}"


def analyze_least_common(all_numbers, all_powerballs):
    counter_numbers = Counter(all_numbers)
    least_common_numbers = counter_numbers.most_common()[-5:]
    counter_powerballs = Counter(all_powerballs)
    least_common_powerball = counter_powerballs.most_common()[-1:]

    return f"5 самых редко выпадающих чисел: {', '.join(num[0] for num in reversed(least_common_numbers))}\nСамый редко выпадающий Powerball: {least_common_powerball[0][0]}"


def analyze_random():
    random_numbers = sorted(random.sample(range(1, 70), 5))
    random_powerball = random.randint(1, 26)

    return f"5 случайных чисел: {', '.join(str(num) for num in random_numbers)}\nСлучайный Powerball: {random_powerball}"


def analyze_powerball_data(file_path, method):
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

    # Call the chosen method
    if method == "most_common":
        result = analyze_most_common(all_numbers, all_powerballs)
    elif method == "least_common":
        result = analyze_least_common(all_numbers, all_powerballs)
    elif method == "random":
        result = analyze_random()

    # Display the results in a new window
    results_window = Toplevel(root)
    results_window.title("Результаты анализа")

    results_frame = tk.Frame(results_window, padx=10, pady=10)
    results_frame.pack()

    result_label = tk.Label(results_frame, text=result)
    result_label.pack()

    results_window.mainloop()


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
    if file_path:
        open_method_window(file_path)


def open_method_window(file_path):
    method_window = Toplevel(root)
    method_window.title("Выберите метод анализа")

    method_frame = tk.Frame(method_window, padx=10, pady=10)
    method_frame.pack()

    most_common_button = tk.Button(method_frame, text="Самые частые числа", command=lambda: analyze_powerball_data(file_path, "most_common"))
    most_common_button.pack(pady=(0, 10))

    least_common_button = tk.Button(method_frame, text="Самые редкие числа",
                                    command=lambda: analyze_powerball_data(file_path, "least_common"))
    least_common_button.pack(pady=(0, 10))

    random_button = tk.Button(method_frame, text="Случайные числа",
                              command=lambda: analyze_powerball_data(file_path, "random"))
    random_button.pack()

    method_window.mainloop()


# Create the tkinter GUI
root = tk.Tk()
root.title("Powerball Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

select_button = tk.Button(frame, text="Выберите файл с данными Powerball", command=select_file)
select_button.pack(pady=(0, 10))

root.mainloop()

