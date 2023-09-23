# CRUD_test_task
Простой сервис для обработки запросов на бронирование времени. Сервис предоставляет функциональность CRUD

## Оглавление
1. [Api](#Docs)
2. [Структура](#Структура-Api)

## requirements

+ `bcrypt` ~=4.0.1
+ `fastapi` ~=0.100.0
+ `pydantic` ~=1.10.12
+ `requests` ~=2.28.1
+ `uvicorn` >=0.15.0,<0.16.0
+ `unittest` ~=3.11.5


## Установка

Для установки без Docker

```cli
git clone https://github.com/Igor20264/CRUD_test_task
cd CRUD_test_task
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Для установки с Docker
```cli
git clone https://github.com/Igor20264/CRUD_test_task
cd CRUD_test_task
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Docs
- После запуска в докере, открыть [Ссылку](http://localhost:8000/docs) (http://localhost:8000/docs) или [Эту](http://localhost:8000/reboc) (http://localhost:8000/reboc) для просмотра Api.

## Структура Api

- /docs
- /redoc

- /user
	- /add
  - /checkname
  - /getid
	- /getall
	- /{user_id}
		- /del
		- /get_reg_time
		- /reset_password


- /booking
  - /add
  - /{user_id}
    - /getall
    - /{booking_id}
      - /del
      - /update

