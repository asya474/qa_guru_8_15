from pages.registration_page import RegistrationPage
from data.users import User



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
        registration_page = RegistrationPage()
        registration_page.open()
        registration_page.register(user=user)
        registration_page.should_have_registered(user)
