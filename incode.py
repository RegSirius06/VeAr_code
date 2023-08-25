import random

import gens

def run():
    Alfabet = ''.join([chr(ord('а') + x) for x in range(32)])
    print(f"\nПример ключа для сообщения: {gens.key_gen()}\n")
    Key = input('Введите ключ для шифрования (русские строчные буквы длиной 32 символа): ')

    message = input('Введите шифруемое сообщение: ')
    messagelist = [x.lower() for x in message if x.isalpha()]

    digit = random.randint(1000, 9999)
    shift = gens.gen_shift(len(messagelist), digit)

    for i in range(len(messagelist)):
        messagelist[i] = Key[(Alfabet.find(messagelist[i]) + shift[i]) % len(Key)]

    code_message = str(digit)[:2] + ''.join(messagelist) + str(digit)[2:]

    print(code_message)
