# WORKPLACE
![Статус проекта: В разработке](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%92%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B5-brightgreen.svg)
### Описание
WORKPLACE — онлайн-платформа для розничной торговли, предлагающая широкий ассортимент высококачественных товаров для удовлетворения ваших повседневных потребностей.

### Используемые технологии:
- Python 3.11
- Django 4.1
- PostgreSQL 15
- Pillow 9.2
### Как развернуть проект локально:
Клонируйте репозиторий:
```
     git clone https://github.com/devbkd/myshop.git
```
или используйте SSH-ключ:
```
     git clone git@github.com:devbkd/myshop.git
```
Установить и активировать виртуальную среду
```
     python -m venv venv
```
```
     source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt
```
     pip install -r requirements.txt
```
Сделать миграцию:
```
     python manage.py migrate
```
Запустите проект в режиме разработки:
```
     cd myshop/  
```
```
     python manage.py runserver
```
Откройте в своем браузере `localhost` или `127.0.0.1:8000`

## Автор:
Рузал Закиров [GitHub](https://github.com/devbkd/)