from model.tinkoff_page import TinkoffPage
import allure

tinkoff_page = TinkoffPage()


def test_debet_cart_tinkoff_black_button(setup_browser):
    tinkoff_page.open()
    with allure.step("Нажать на кнопку"):
        tinkoff_page.tinkoff_black_button()
    with allure.step("Происходит переадресация на другую страницу"):
        tinkoff_page.go_to_tinkoff_black_button_page()

def test_deposits_button(setup_browser):
    tinkoff_page.open()
    with allure.step("Нажать на кнопку"):
        tinkoff_page.deposits_button()
    with allure.step("Происходит переадресация на другую страницу"):
        tinkoff_page.go_to_deposits_button_page()

def test_investition_button(setup_browser):
    tinkoff_page.open()
    with allure.step("Нажать на кнопку"):
        tinkoff_page.investition_button()
    with allure.step("Происходит переадресация на другую страницу"):
        tinkoff_page.go_to_investition_button_page()

def test_insurance_button(setup_browser):
    tinkoff_page.open()
    with allure.step("Нажать на кнопку"):
        tinkoff_page.insurance_button()
    with allure.step("Происходит переадресация на другую страницу"):
        tinkoff_page.go_to_insurance_button_page()

def test_travel_button(setup_browser):
    tinkoff_page.open()
    with allure.step("Нажать на кнопку"):
        tinkoff_page.travel_button()
    with allure.step("Происходит переадресация на другую страницу"):
        tinkoff_page.go_to_travel_button_page()

