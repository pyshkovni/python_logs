
# Логирование

# импорт фреймворка logging
import logging
from handlers import prime_numbers_generator, divide


def print_primes(n):
    for prime in prime_numbers_generator(n):
        logging.info(f'Простое из генераторов {prime}')


# Конфигурации логирования
# Запись сообщений в лог по умолчанию
# Будут записываться все сообщения выше выбранного уровня
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

# # Запись вывода в файл
# logging.basicConfig(
#     level=logging.DEBUG,
#     handlers=[logging.FileHandler('primes.log', 'w', 'utf-8')],
# )
# или
# logging.basicConfig(level=logging.DEBUG, filename='primes.log')
# Обратите внимание, что логирование происходит в нескольких модулях

# логирование в несколько мест
# проблема! при логировании нескольких объектов определен один файл.
# разобраться, какое сообщение откуда пришло, затруднительно.
# поэтому, сообщения в логах нужно разделять
# Для этого можно создавать объекты логирования и конфигурировать их
# например, информационные сообщения записываются в один лог, а ошибки в другой

# log = logging.getLogger('divide')
# log.setLevel(logging.INFO)
# fh = logging.FileHandler("divide.log", 'w', 'utf-8')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # все возможные аттрибуты см https://docs.python.org/3.5/library/logging.html#logrecord-attributes
# fh.setFormatter(formatter)
# log.addHandler(fh)

# TODO – Опишите объект логирования для функции prime_numbers_generator, так,
#  чтобы сообщения из main писались в main.log, а сообщения из handlers писались в handlers.log

# для того, чтобы удобнее управлять логированием, необходим файл конфигурации логера
# такой файл представлен в log_settings

# переместите в импорты
# import logging
# import logging.config
# from log_settings import log_config

# logging.config.dictConfig(log_config)
# log = logging.getLogger('')

# TODO - создайте логирование main и handlers через конфигуратор


if __name__ == '__main__':
    # работа генератора простых чисел
    print(print_primes(n=10))

    # работа функции деления на нуль
    number = 50
    try:
        logging.info('Запуск функции divide')
        divide(number)
        logging.info('divide вернул значение!')
    except Exception:
        logging.exception(f'Ошибка при работе с {number}')
