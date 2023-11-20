# Проект по тестированию сайта "Tinkoff"


### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами браузера
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах в Jira
* Запуск автотестов в Selenoid

### Список проверок, реализованных в автотестах

- [x] Перейти на страницу Кредиты возможно
- [x] Перейти на страницу Вклады возможно
- [x] Перейти на страницу Инвестиции возможно
- [x] Перейти на страницу Страховка возможно
- [x] Перейти на страницу Путешествия возможно

----

### Используемый стэк

<table border="2">
  <tbody>
    <tr>
        <td>Python</td>
        <td>Pytest</td>
        <td>Selene</td>
        <td>Selenium</td>
        <td>Selenoid</td>
        <td>Jenkins</td>
        <td>Allure Reports</td>
        <td>Allure TestOps</td>
        <td>Jira</td>
    </tr>
  </tbody>
</table>

<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenium.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----

### Локальный запуск автотестов

#### Выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/Saber-Interactive-Auto-Tests/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
BROWSER_VERSION = 100 # Версия браузера
ENVIRONMENT = ['STAGE', 'PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Saber-Interactive-Auto-Tests/">проект</a>

![jenkins project main page](qa_guru_python_8_15/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. В поле "BROWSER_VERSION" ввести: 100
4. Из списка "ENVIRONMENT" выбрать: PROD
5. В поле "COMMENT" ввести комментарий
6. Нажать "Build"

![jenkins_build](qa_guru_python_8_15/pictures/jenkins_build.png)

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](qa_guru_python_8_15/pictures/allure_report_overview.png)

#### Результаты прохождения теста
![allure_reports_behaviors](qa_guru_python_8_15/pictures/allure_reports_behaviors.png)

#### Графики

![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3782/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](qa_guru_python_8_15/pictures/allure_testops_dashboards.png)

#### История запуска тестовых наборов

![allure_testops_launches](qa_guru_python_8_15/pictures/allure_testops_launches.png)

#### Тест кейсы

![allure_testops_suites](qa_guru_python_8_15/pictures/allure_testops_suites.png)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-953">Ссылка на проект</a>

![jira_project](qa_guru_python_8_15/pictures/jira_project.png)

----

### Оповещения в Telegram
![telegram_allert](qa_guru_python_8_15/pictures/telegram_allert.png)

----

### Видео прохождения автотеста
![autotest_gif](qa_guru_python_8_15/pictures/autotest.gif)

----

### Mind map тест плана

![allure_reports_graphs](qa_guru_python_8_15/pictures/test-case-mind-map.png)
