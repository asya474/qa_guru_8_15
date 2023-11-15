from model.tinkoff_page import TinkoffPage
from data.users import User
import allure
from selene import browser, be, have

tinkoff_page = TinkoffPage()


def test_debet_cart_tinkoff_black_button(setup_browser):
    with allure.step("Открыть главную страницу"):
        browser.element('#cbEZbIs7E').click()
        browser.should(have.url_containing(
            f'/cards/debit-cards/tinkoff-black/?internal_source=home_slider_block'
        ))

def test_deposits_button(setup_browser):
    with allure.step("Открыть главную страницу"):
        browser.element('#cbn4iE95H').click()
        browser.should(have.url_containing(
            f'/savings/deposit/?internal_source=home_icon'
        ))

def test_investition_button(setup_browser):
    with allure.step("Открыть главную страницу"):
        browser.element('#cbn4iE95H').click()
        browser.should(have.url_containing(
            f'/invest/?internal_source=home_icon'
        ))

def test_insurance_button(setup_browser):
    with allure.step("Открыть главную страницу"):
        browser.element('#cbn4iE95H').click()
        browser.should(have.url_containing(
            f'/insurance/?internal_source=home_icon'
        ))

def test_travel_button(setup_browser):
    with allure.step("Открыть главную страницу"):
        browser.element('#cbn4iE95H').click()
        browser.should(have.url_containing(
            f'/travel/?internal_source=home_icon'
        ))

