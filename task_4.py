"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

cache = set()

while True:
    url = input('Введите url (остановить -> no): ')
    salt = 'some_salt'
    hash_url = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
    if url == 'no':
        print('Скрипт остановлен')
        print(cache)
        break
    elif hash_url in cache:
        print('Странице есть в кеше')
        print(cache)
    else:
        cache.add(hash_url)
        print('Страница добавлена в кеш')
        print(cache)