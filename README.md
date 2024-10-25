# Luma Project Test Suite

## Описание

Этот проект содержит автоматизированные тесты для тестирования тестового
сайта https://magento.softwaretestingboard.com/. Тесты написаны с использованием Python и библиотеки Selenium.

## Структура проекта

- `base/` - Директория, содержащая base_test.py и base_page.py.
- `data/` - Директория, содержащая файлы с данными.
- `pages/` - Директория, содержащая Page Object модели для различных страниц сайта Luma.
- `tests/` - Директория, содержащая все тестовые файлы.
- `conftest.py` - Файл конфигурации pytest, содержащий инициализацию browser.
- `requirements.txt` - Файл зависимостей проекта.
- `pytest.ini` - Файл описывающий маркеры pytest для запуска определенных групп тестов.
- `README.md` - Этот файл.

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/IrinaFrutiz/LumaProject
     ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    ```
    
    Для Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
   
   Для Windows:
   ```bash
    venv/Scripts/activate.ps1
    ```
   
4. **Установите зависимости:**
   
   ```bash
    pip install -r requirements.txt
   ```

5. **Запуск тестов**
   Для того, чтобы запустить все тесты, выполните следующую команду в корне проекта:

    ```bash
    pytest
    ```

   Для запуска тестов с генерацией отчета Allure:

Установите Allure CLI. Запустите тесты с генерацией отчета:

    pytest --alluredir=allure-results
    allure serve allure-results

## Allure report on GitHub

Посмотреть последний репорт можно по [ссылке](https://irinafrutiz.github.io/LumaProject/).

## Структура тестов

Тесты разделены на логические группы и находятся в соответствующих файлах внутри директории tests/.
Присутствует файл base/base_test.py, который облегчает обращение к page в тестах.

## Page Object Model (POM)

Этот проект использует паттерн Page Object Model для организации кода. Все модели страниц находятся в директории pages/.
Базовая страница находится в base/base_page.py, в которой описаны основные действия на странице.

## Вклад в проект

Все предложения по улучшению проекта приветствуются!
