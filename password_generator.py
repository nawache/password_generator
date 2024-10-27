import secrets
import string


VALID_SYMBOLS = string.ascii_letters + string.digits + '!@#$%^&*()'
ERROR_MESSAGE = ("Значение длины пароля должно быть целым положительным "
                 "числом от 1 до 64.")
POSITIVE_ANSWERS = ("д", "да", "ага", "y", "yes", "yeah")


def generate_password(length, symbols):
    password = ''.join(secrets.choice(symbols) for _ in range(length))
    return password


def get_password_length():
    while True:
        try:
            password_length = int(input("\nВведите длину пароля:\n>: "))
            if password_length > 0 and password_length <= 64:
                return password_length
            else:
                print(ERROR_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)


def main():
    length = get_password_length()
    password = generate_password(length, VALID_SYMBOLS)

    print("\nСгенерированный пароль:", password)
    try_again()


def try_again():
    response = input("\nХотите сгенерировать ещё один пароль? (y/n)\n>: ")
    if response.lower() in POSITIVE_ANSWERS:
        main()
    else:
        print("\nДо свидания!")


if __name__ == "__main__":
    print("Добро пожаловать в генератор паролей!")
    main()
