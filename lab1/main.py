import sys
import math


def read_coefficient(name, value=None):
    if value is not None:
        try:
            return float(value)
        except ValueError:
            print(f"Некорректное значение коэффициента {name}: {value}")

    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка! Введите действительное число.")


def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечно много решений."
            else:
                return "Действительных корней нет."

        y = -c / b

        if y < 0:
            return "Действительных корней нет."
        elif y == 0:
            return "x = 0"
        else:
            x = math.sqrt(y)
            return f"x1 = {x}, x2 = {-x}"

    d = b ** 2 - 4 * a * c

    print(f"Дискриминант D = {d}")

    if d < 0:
        return "Действительных корней нет."

    if d == 0:
        y = -b / (2 * a)

        if y < 0:
            return "Действительных корней нет."
        elif y == 0:
            return "x = 0"
        else:
            x = math.sqrt(y)
            return f"x1 = {x}, x2 = {-x}"

    y1 = (-b + math.sqrt(d)) / (2 * a)
    y2 = (-b - math.sqrt(d)) / (2 * a)

    roots = []

    if y1 > 0:
        x = math.sqrt(y1)
        roots.extend([x, -x])
    elif y1 == 0:
        roots.append(0)

    if y2 > 0:
        x = math.sqrt(y2)
        roots.extend([x, -x])
    elif y2 == 0:
        roots.append(0)

    if not roots:
        return "Действительных корней нет."

    return "Действительные корни: " + ", ".join(map(str, roots))


def main():
    args = sys.argv[1:]

    a = read_coefficient("A", args[0] if len(args) > 0 else None)
    b = read_coefficient("B", args[1] if len(args) > 1 else None)
    c = read_coefficient("C", args[2] if len(args) > 2 else None)

    print(f"\nУравнение: {a}x^4 + ({b})x^2 + ({c}) = 0")
    print(solve(a, b, c))


if __name__ == "__main__":
    main()
