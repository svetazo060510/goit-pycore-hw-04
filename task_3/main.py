import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def display_directory_structure(directory_path: Path, indent_level: int = 0):
    # Створюємо рядок відступу (2 пробіли на рівень)
    indent = "  " * indent_level
    
    try:
        entries = sorted(list(directory_path.iterdir()))
        
        for entry in entries:
            if entry.is_dir():
                # Директорії: синій колір + /
                print(f"{indent}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
                # Рекурсивний виклик зі збільшеним рівнем відступу
                display_directory_structure(entry, indent_level + 1)
            else:
                # Файли: зелений колір
                print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")

    except PermissionError:
        # Обробка помилки доступу
        print(f"{indent}{Fore.RED}Permission denied: {entry.name}{Style.RESET_ALL}")
    except Exception as e:
        # Обробка інших помилок
        print(f"{indent}{Fore.RED}Error reading {entry.name}: {e}{Style.RESET_ALL}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Шлях до директорії не вказаний.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
        return
    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує.")
        return
    
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не є директорією.")
        return

    print(f"\n{Fore.BLUE}{directory_path.name}/{Style.RESET_ALL}")
    
    display_directory_structure(directory_path, indent_level=1)
    print()

if __name__ == "__main__":
    main()