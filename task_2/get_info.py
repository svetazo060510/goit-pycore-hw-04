def get_cats_info(path: str) -> list[dict]:

    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    # Цей блок виконається, якщо в рядку не рівно три елементи
                    print(f"Попередження: Некоректний формат даних: '{line.strip()}'. Рядок буде проігноровано.")

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return [] 
    except Exception as e:
        print(f"Сталася непередбачувана помилка при роботі з файлом: {e}")
        return []

    return cats_info
