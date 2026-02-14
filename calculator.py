# calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def power(a, b):
    return a**b


def divide(a, b):
    return a / b


def main():
    print("=== Калькулятор ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Степень")
    print("5. Деление")
    choice = input("Выберите операцию (1-4): ")

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = power(a, b)
    elif choice == "5":
        result = divide(a, b)
    else:
        print("Ошибка: неверный выбор")
        return

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
