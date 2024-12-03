def is_prime(number):
    is_prime = True
    if number <= 1:
        is_prime = False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        return print(f"{number} Adalah bilangan prima")
    else:
        return print(f"{number} Bukan bilangan prima")


def print_prime_number(number):
    prime_number = []
    for num in range(2, number + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_number.append(num)
    return print(f"dari angka 1 sampai {number}, bilangan prima adalah: {prime_number}")


def print_segitiga_siku(number):
    pyramid = ""
    for i in range(0, number + 1):
        pyramid = pyramid + (i * "*") + "\n"
    return print(pyramid)


def print_segitiga_siku_inverse(number):
    pyramid = ""
    for i in range(number + 1, 0, -1):
        pyramid = (
            pyramid
            + ((number - i + 2) * "-")
            + ((i + (i - 1)) * "|")
            + ((number - i + 2) * "-")
            + "\n"
        )
    return print(pyramid)


def print_pyramid(number):
    pyramid = ""
    for i in range(1, number + 1):
        pyramid = (
            pyramid
            + ((number - i + 2) * "-")
            + ((i + (i - 1)) * "|")
            + ((number - i + 2) * "-")
            + "\n"
        )
    return print(pyramid)


def print_pyramid_terbalik(number):
    pyramid = ""
    for i in range(number + 1, 0, -1):
        pyramid = (
            pyramid
            + ((number - i + 2) * "-")
            + ((i + (i - 1)) * "|")
            + ((number - i + 2) * "-")
            + "\n"
        )
    return print(pyramid)


number_input = int(input("Masukkan Angka: "))
print(f"angka yang anda masukkan = {number_input}")
# print_pyramid(number_input)
is_prime(number_input)
print_prime_number(number_input)
