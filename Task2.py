# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.

from collections import deque

def check_palindrom(word):
    wdeque = deque(word.lower().replace(' ', ''))
    if len(wdeque) % 2 == 0:
        n = 0
    else:
        n = 1
    while len(wdeque) != n:
        if wdeque.popleft() != wdeque.pop():
            return False
    return True

def main():
    words = ["ABBA", "Ab B a", "Ab b_a", "Tenet", "qUe_u e"]
    for word in words:
        print(f"Word {word} is{" NOT " if not check_palindrom(word) else ' '}palindrom")

if __name__ == "__main__":
    main() 