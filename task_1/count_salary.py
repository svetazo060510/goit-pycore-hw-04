import pathlib

def total_salary(path: str) -> tuple[float, float]:
    
    file_path = pathlib.Path(path)
    try:
        total_sum = 0.0
        developer_count = 0

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary_str = line.strip().split(',')
                    salary = float(salary_str)
                    
                    total_sum += salary
                    developer_count += 1
                except ValueError:
                    print(f"Warning: A line was ignored: '{line.strip()}'")

        if developer_count == 0:
            return 0.0, 0.0

        average_salary = total_sum / developer_count    
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
        return 0.0, 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0, 0.0