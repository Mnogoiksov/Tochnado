import csv
import random
import statistics
from collections import Counter
import tkinter as tk
from tkinter import filedialog, Toplevel


def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    stdev = statistics.stdev(numbers)
    return mean, median, mode, stdev


def analyze_statistics(all_numbers, all_powerballs):
    numbers_mean, numbers_median, numbers_mode, numbers_stdev = calculate_statistics(all_numbers)
    powerballs_mean, powerballs_median, powerballs_mode, powerballs_stdev = calculate_statistics(all_powerballs)

    result = f"Статистика для обычных чисел:\nСреднее: {numbers_mean:.2f}\nМедиана: {numbers_median}\nМода: {numbers_mode}\nСтандартное отклонение: {numbers_stdev:.2f}\n\nСтатистика для Powerball:\nСреднее: {powerballs_mean:.2f}\nМедиана: {powerballs_median}\nМода: {powerballs_mode}\nСтандартное отклонение: {powerballs_stdev:.2f}"
    return result


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
        for x in row[1:6]:
            try:
                all_numbers.append(int(x))
            except ValueError:
                print(f"Skipping invalid value: {x}")
        for x in row[6:7]:
            try:
                all_powerballs.append(int(x))
            except ValueError:
                print(f"Skipping invalid value: {x}")

    # Call the chosen method
    if method == "statistics":
        result = analyze_statistics(all_numbers, all_powerballs)

    # Display the results in a new window
    results_window = Toplevel(root)
    results_window.title("Результаты анализа")

    results_frame = tk.Frame(results_window, padx=10, pady=10)
    results_frame.pack()

    result_label = tk.Label(results_frame, text=result, justify="left")
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

    statistics_button = tk.Button(method_frame, text="Статистика", command=lambda: analyze_powerball_data(file_path, "statistics"))
    statistics_button.pack(pady=(0, 10))

    method_window.mainloop()


# Create the tkinter GUI
root = tk.Tk()
root.title("Powerball Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

select_button = tk.Button(frame, text="Выберите файл с данными Powerball", command=select_file)
select_button.pack(pady=(0, 10))

root.mainloop()
