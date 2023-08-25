from incode import run as in_run
from decode import run as de_run

x = -1
while x != 0:
    while True:
        i = input('Выберите действие, которое необходимо сделать:\n\n'
                  'Если вы хотите закодировать сообщение, введите 1;\n'
                  'Если вы хотите декодировать сообщение, введите 2;\n'
                  'Если хотите завершить программу, введите 0.\n\n'
                  'Введите число: ')
        if i.isdigit(): break
    x = int(i)
    match x:
        case 0: pass
        case 1: in_run()
        case 2: de_run()
        case _: print('\nПожалуйста, введите правильное число.\n')
