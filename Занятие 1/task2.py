#task2 - Грачева Екатерина
number = int(input())

max_number = int(input())

if number > max_number * 3:
    print('Произвольное число больше пограничного более, чем в 3 раза')
elif number > max_number:
    print('Произвольное число больше пограничного')
elif number < max_number:
    print('Произвольное число меньше пограничного')
