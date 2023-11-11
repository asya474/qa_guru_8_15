from model.practice_form_full import PracticeFormRegistrationFactCheck
from data.users import User
import allure

practice_form = PracticeFormRegistrationFactCheck()


def test_student_registration_form(setup_browser):
    with allure.step("Открыть страницу регистрации пользователей"):
        practice_form.open()
    with allure.step("Заполнить форму регистрации тестовыми данными"):
        guest = User(first_name='Имя',
                     last_name='Фамилия',
                     email='testmail@mail.gg',
                     gender='Other',
                     month_of_birth='November',
                     phone_number='2589632147',
                     year_of_birth='2006',
                     day_of_birth='19',
                     subject='Physics',
                     hobby='Reading',
                     image='hedgehog.jpg',
                     address='221b, Baker Street, London, NW1 6XE, UK',
                     state='NCR',
                     city='Delhi')
        practice_form.registration(guest)
    with allure.step("Проверка, что пользователь зарегистрирован"):
        practice_form.student_should_be_registred(guest)
