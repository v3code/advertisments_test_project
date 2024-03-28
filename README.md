# Тестовое задание для backend-стажёра в команду Advertising

## Задача
Необходимо создать сервис для хранения и подачи объявлений. Объявления должны храниться в базе данных. Сервис должен предоставлять API, работающее поверх HTTP в формате JSON.

## Требования
* Язык программирования Go/PHP — очень желательно, так как это основные языки для нас (больше Go), но в целом мы не ограничиваем вас;
* Финальную версию нужно выложить на github.com (просьба не делать форк этого репозитория, дабы не плодить плагиат);
* Простая инструкция для запуска (в идеале — с возможностью запустить через `docker-compose up`, но это необязательно);
* 3 метода: получение списка объявлений, получение одного объявления, создание объявления;
* Валидация полей: не больше 3 ссылок на фото, описание не больше 1000 символов, название не больше 200 символов;

Если есть сомнения по деталям — решение принять самостоятельно, но в своём README.md рекомендуем выписать вопросы и принятые решения по ним.

## Детали
**Метод получения списка объявлений**
* Пагинация: на одной странице должно присутствовать 10 объявлений;
* Cортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание);
* Поля в ответе: название объявления, ссылка на главное фото (первое в списке), цена.

**Метод получения конкретного объявления**
* Обязательные поля в ответе: название объявления, цена, ссылка на главное фото;
* Опциональные поля (можно запросить, передав параметр fields): описание, ссылки на все фото.

**Метод создания объявления:**
* Принимает все вышеперечисленные поля: название, описание, несколько ссылок на фотографии (сами фото загружать никуда не требуется), цена;
* Возвращает ID созданного объявления и код результата (ошибка или успех).

## Усложнения
Не обязательно, но задание может быть выполнено с любым числом усложнений:
* Юнит тесты: постарайтесь достичь покрытия в 70% и больше;
* Контейнеризация: есть возможность поднять проект с помощью команды `docker-compose up`;
* Архитектура сервиса описана в виде текста и/или диаграмм
* Документация: есть структурированное описание методов сервиса.


# Стэк
- Flask
- Postgres
- Docker
- SQLAlchemy



## Как запустить

Запуск производиться через команду poetry run run-server

