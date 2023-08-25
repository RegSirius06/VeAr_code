import gens


def run():
    Alfabet = ''.join([chr(ord('а') + x) for x in range(32)])
    print(f"\nПример ключа для сообщения: {gens.key_gen()}\n")
    Key = input('Введите ключ для шифрования (русские строчные буквы длиной 32 символа): ')

    message = input('Введите зашифрованное сообщение: ')
    messagelist = [x for x in message]

    digit = int(''.join(messagelist[:2]) + ''.join(messagelist[-2:]))
    messagelist = messagelist[2:-2]
    shift = gens.gen_shift(len(messagelist), digit)

    for i in range(len(messagelist)):
        messagelist[i] = Alfabet[(Key.find(messagelist[i]) - shift[i]) % len(Alfabet)]

    print("".join(messagelist))
