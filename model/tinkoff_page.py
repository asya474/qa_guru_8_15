from selene import browser, have, by


class TinkoffPage:

    def credit_cart_button(self):
        browser.element('[href = "/cards/credit-cards/?internal_source=home_icon"]').press_enter()

    def deposits_button(self):
        browser.element('[href = "/savings/deposit/?internal_source=home_icon"]').press_enter()

    def investition_button(self):
        browser.element('[href = "/invest/?internal_source=home_icon"]').press_enter()

    def insurance_button(self):
        browser.element('[href = "/insurance/?internal_source=home_icon"]').press_enter()

    def travel_button(self):
        browser.element('[href = "/travel/?internal_source=home_icon"]').press_enter()

    def go_to_credit_cart_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/cards/credit-cards/?internal_source=home_icon'
        ))

    def go_to_deposits_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/savings/deposit/?internal_source=home_icon'
        ))

    def go_to_investition_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/invest/?internal_source=home_icon'
        ))

    def go_to_insurance_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/insurance/?internal_source=home_icon'
        ))

    def go_to_travel_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/travel/?internal_source=home_icon'
        ))
