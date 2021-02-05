# News_portal
Задача: реализовать API для новостного портала 

Технологии: 
 - Python3 
 - Django
 - СУБД PostgreSQL (через отдельный docker образ)
 - Контейнер с приложением на alpine
 - Описание API - Swagger OpenApi Version 3

## Installation guide
```
cd simbirsoft_test_task
docker-compose up --build
```
Для создания суперпользователя необходимо войти в запущенный контйнер
```
docker exec -it web_simbirsoft_container bash
python3 manage.py createsuperuser
```

Вход в админку:
127.0.0.1:8000/admin/

## Создание пользователя

http://127.0.0.1:8000/auth/users/ (ввести username, почту пароль и отправить post запрос)

После post запроса на указанную при регистрации почту придет письмо, которые будет содержать ссылку с uid и token. Пример: http://127.0.0.1:8000/#/activate/MjA3/ahj9ec-0883dba0434bf57525725e586cbab31

ahj9ec-0883dba0434bf57525725e586cbab31 - token

MjA3 - uid

Для подтверждения email необходимо отправить post запрос с uid  и token по адресу: http://127.0.0.1:8000/auth/users/activation/

*** отправка email реализована через консоль, т.е. в консоли вы увидите все отправленные email с нужной информацией

## API documentation

### Swagger Open API

Для входа в документацию swagger необходимо при запущенном контейнере перейти по ссылке http://127.0.0.1:8000/api/docs/
Документация построена с помощью библиотеки drf_spectacular (данная библиотека наоборот расставляет значки "замочка", который отвечает за права доступа пользователя к этому url)

#### JWT-token

Для тестирования api приложения необходимо выписать себе jwt-token, для этого нужно перейти по адресу

http://127.0.0.1:8000/auth/jwt/create/ 

отправить post запрос с логином и паролем далее использовать этот token

*** API реализовано согласно ТЗ, с учетом прав доступа и описано в Swagger.
