from math import gcd


def start():
    while True:
        n = str(input("Введи атуральное число больше 1: "))
        if n.isdigit() and n not in ["0", "1"]:
            print(", ".join([i[1] for i in find_fractions(int(n))]))
        else: print("Ошибка! Попробуй еще раз")


def find_fractions(n):
    list_fractions = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if gcd(i, j) == 1:
                list_fractions.append((i / j, f"{i}/{j}"))
    list_fractions.sort(key=lambda x: x[0])
    return list_fractions


if __name__ == "__main__":
    start()