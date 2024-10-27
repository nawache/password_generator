import string
import random


valid_symbols = string.ascii_letters + string.digits + '!@#$%^&*()'
ERROR_MESSAGE = ("Значение длины пароля должно быть целым положительным "
                 "числом от 1 до 64.")


def generate_password(length, symbols):
    password = ''.join(random.choice(symbols) for _ in range(length))
    return password


def get_password_length():
    while True:
        try:
            length = int(input("\nВведите длину пароля:\n>: "))
            if length > 0 and length <= 64:
                return length
            else:
                print(ERROR_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)


def main():
    length = get_password_length()
    password = generate_password(length, valid_symbols)

    print("\nСгенерированный пароль:", password)
    try_again()


def try_again():
    POSITIVE_ANSWERS = ("д", "да", "ага", "y", "yes", "yeah")

    response = input("\nХотите сгенерировать ещё один пароль? (y/n)\n>: ")
    if response.lower() in POSITIVE_ANSWERS:
        main()
    else:
        print("\nДо свидания!")


if __name__ == "__main__":
    print("Добро пожаловать в генератор паролей!")
    main()
