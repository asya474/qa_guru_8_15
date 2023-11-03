import allure
from allure_commons.types import Severity

from tests_demo.data import users_data
from tests_demo.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "a.shemetova")
@allure.description("Test with allure steps")
@allure.feature("Search issue on github")
@allure.link('https://demoqa.com', name='Testing')
def test_submit_student_registration_form_by_high_steps():
    registration_page = RegistrationPage()
    user = users_data.Charles_Leclerc

    with allure.step("Open form"):
        registration_page.open_form()
    with allure.step("Fill the form"):
        registration_page.submit_form(user)
    with allure.step("Check form results"):
        registration_page.should_have_registrated_user(user)