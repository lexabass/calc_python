import math

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Делить на ноль нельзя!"
    return x / y

def main():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: некорректный ввод. Пожалуйста, введите числа.")
            continue

        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")

        choice = input("Введите номер операции (1/2/3/4): ")

        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {divide(num1, num2)}")
        else:
            print("Ошибка: некорректный выбор операции.")

        next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
        if next_calculation.lower() != 'да':
            break

if __name__ == "__main__":
    main()
