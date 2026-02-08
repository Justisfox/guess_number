
from random import randint


number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    
    guess = int(input('Введите число: '))
    
    # Если число меньше загаданного...
    if guess < number:
        print('Ваше число меньше того, что загадано.')
    
    if guess > number:
        print('Ваше число больше того, что загадано.')
    print('fdff')
    # Если число угадано...
    if guess == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')
