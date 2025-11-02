class Calculator:
    def add(self, a, b):
        """Додавання двох чисел"""
        return a + b

    def subtract(self, a, b):
        """Віднімання двох чисел"""
        return a - b

    def multiply(self, a, b):
        """Множення двох чисел"""
        return a * b

    def divide(self, a, b):
        """Ділення двох чисел"""
        if b == 0:
            raise ValueError("Ділення на нуль неможливе")
        return a / b


def main():
    calc = Calculator()
    print("Простий калькулятор")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")


if __name__ == "__main__":
    main()

