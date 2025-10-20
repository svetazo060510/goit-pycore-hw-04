import pathlib
from count_salary import total_salary

total, average = total_salary("/Users/admin/homeworks/goit-pycore-hw-04/task_1/salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")