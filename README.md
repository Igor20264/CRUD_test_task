# CRUD_test_task
Простой сервис для обработки запросов на бронирование времени. Сервис предоставляет функциональность CRUD

## Оглавление
1. [Установка](#Установка)
2. [Документация](#Документация)

## requirements

+ `bcrypt` ~=4.0.1
+ `fastapi` ~=0.100.0
+ `pydantic` ~=1.10.12
+ `edgedb` ~=1.7.0
+ `uvicorn` >=0.15.0,<0.16.0

## Технологии

База данных: edgedb


## Установка

Для установки без Docker

```cli
git clone https://github.com/Igor20264/CRUD_test_task
cd CRUD_test_task
edgedb project init
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```
> **Warning**
> Docker Временно не поддерживается
> 
Для установки в Docker
```cli
echo Erorr
#git clone https://github.com/Igor20264/CRUD_test_task
#docker build -t crud_test CRUD_test_task
#docker run crud_test
```

## Docs
- После запуска в докере, открыть [Ссылку](http://localhost:8000/docs) (http://localhost:8000/docs) или [Эту](http://localhost:8000/reboc) (http://localhost:8000/reboc) для просмотра Api.