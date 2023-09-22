# CRUD_test_task
Простой сервис для обработки запросов на бронирование времени. Сервис предоставляет функциональность CRUD


## Docs
- После запуска в докере, открыть [Ссылку](http://localhost:8000/docs) (http://localhost:8000/docs) для просмотра Api


## Ниже задача будет разбита на подзадачи, которые вам предстоит выполнить:
### Основная часть:
6. Контейнеризация приложения при помощи Docker.
8. Написание автоматических тестов для созданного функционала.
9. 
- Проект содержит Dockerfile для запуска в Docker
## Критерии оценки
*Критерии отсортированы по важности при оценивании (по убыванию)*

1. Получилось ли запустить программу с первого раза по инструкциям в README.md и
получилось ли воспроизвести результаты
4. Репозиторий не содержит бинарных артефактов сборки.

## Структура Api (Временное)
- /user
	- /get_id_name [<- name] | [-> int (user id)]
	- /add [<- name, password] | [-> int (user id)]
	- /getall [-> list (name,user id)]
	- /{user_id}
		- /del [password <-] | [-> bool]
		- /get_reg_time [password <-] | [-> time (В мс.)]
		- /reset_password [<- time_create or time_updated] | [->  bool]


- /booking
  - /getall [-> list (booking id,user id)]
  - /{user}
    - /tall [-> list (booking id)]
    - /add [start,duration,comment(optional) <-] | [-> id]
    - /{booking_id}
      - /del [password <-] | [-> bool]
      - /update [password,start,duration,comment(optional) <-] | [-> bool]

