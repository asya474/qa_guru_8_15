# Проект по тестированию сайта "Tinkoff"
> <a target="_blank" href="https://cyber.games/">Saber Interactive</a>

![main page screenshot](/qa_guru_python_8_15/pictures/main_page.jpg)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами браузера, DOM моделью страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах в Jira
* Запуск автотестов в Selenoid

### Список проверок, реализованных в автотестах

- [x] Раздел 'About' отображается
- [x] Перейти к игровому проекту возможно
- [x] Перейти к студии возможно
- [x] Перейти к новости возможно
- [x] Перейти в раздел 'Careers' возможно
- [x] Отправить контакты возможно

----

### Используемый стэк

<img title="Python" src="qa_guru_python_8_15/pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="qa_guru_python_8_15/pictures/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="qa_guru_python_8_15/pictures/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="qa_guru_python_8_15/pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="qa_guru_python_8_15/pictures/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="qa_guru_python_8_15/pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="qa_guru_python_8_15/pictures/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="qa_guru_python_8_15/pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="qa_guru_python_8_15/pictures/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="qa_guru_python_8_15/pictures/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="qa_guru_python_8_15/pictures/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="qa_guru_python_8_15/pictures/icons/jenkins-original.svg" height="40" width="40"/>

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
