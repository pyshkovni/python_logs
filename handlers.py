# импорт фреймворка logging
import logging


def prime_numbers_generator(n):
    """
    The generator looks for numbers in a sequence up to n that are divisible by an integer primes

    :param n:
    :return:
    """
    prime_numbers = []
    for number in range(2, n + 1):
        logging.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                logging.debug(f'делится на {prime}')
                break
        else:
            logging.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


def divide(param):
    """
    The division function by ... what?

    :param param:
    :return:
    """
    return param / 0
