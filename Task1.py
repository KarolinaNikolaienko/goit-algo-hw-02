# Завдання 1

# Потрібно розробити програму, яка імітує приймання й обробку заявок:
# програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними),
# додавати їх до черги, а потім послідовно видаляти з черги для "обробки",
# імітуючи таким чином роботу сервісного центру.

import time
from queue import Queue
from random import randint


#Створити чергу заявок
queue = Queue()
i = 1

def generate_request():
    #Створити нову заявку
    global i
    request = f'Request {i}'
    i += 1
    #Додати заявку до черги
    queue.put(request)
    print(f"{request} has been added")

def process_request():
    #Якщо черга не пуста:
    if not queue.empty():
        #Видалити заявку з черги
        request = queue.get()
        #Обробити заявку
        print(f"Processing a {request}...")
        time.sleep(randint(0, 5))
        print(f"{request} processed successfully")
    #Інакше:
    else:
        print('The queue is EMPTY')
        #Вивести повідомлення, що черга пуста

def main():
    #Головний цикл програми:
    #Поки користувач не вийде з програми:
    print("---PRESS CTRL + C TO EXIT---")
    while True:
        #Виконати generate_request() для створення нових заявок
        time.sleep(randint(0,5))
        generate_request()
        process_request()
        #Виконати process_request() для обробки заявок

if __name__ == "__main__":
    main()