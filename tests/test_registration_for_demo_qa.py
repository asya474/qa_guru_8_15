from pages.registration_page import RegistrationPage
from data.users import User
import allure


@allure.title("Successful registration form")
def test_registration_form(setup_browser):
    with allure.step("User data"):
        user = User('Test',
                    'Test',
                    'test@test.com',
                    'Male',
                    '1234567890',
                    '2001',
                    'May',
                    '15',
                    'Computer Science',
                    'Reading',
                    'character.png',
                    'Sugar Palace, a candy store in Ponyville',
                    'NCR',
                    'Delhi')
    with allure.step("Receive example of Registration page class"):
        registration_page = RegistrationPage()
    with allure.step("Open registration form"):
        registration_page.open()
    with allure.step("Register our user"):
        registration_page.register(user=user)
    with allure.step("Our user should be registered"):
        registration_page.should_have_registered(user)
