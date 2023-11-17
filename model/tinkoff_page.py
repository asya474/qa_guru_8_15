from selene import browser, have, by


class TinkoffPage:
    def open(self):
        browser.open('https://www.tinkoff.ru/')

    def tinkoff_black_button(self):
        browser.element('ab3z6E84Q abYZE7Woe nb3z6E84Q rb3z6E84Q sb3z6E84Q').click()

    def deposits_button(self):
        browser.element(by.text('Вклады')).click()

    def investition_button(self):
        browser.element('cbn4iE95H').click()

    def insurance_button(self):
        browser.element('cbn4iE95H').click()

    def travel_button(self):
        browser.element('#cbn4iE95H').click()

    def go_to_tinkoff_black_button_page(self):
        browser.should(have.url_containing(
            f'/cards/debit-cards/tinkoff-black/?internal_source=home_slider_block'
        ))

    def go_to_deposits_button_page(self):
        browser.should(have.url_containing(
            f'/savings/deposit/?internal_source=home_icon'
        ))

    def go_to_investition_button_page(self):
        browser.should(have.url_containing(
            f'/invest/?internal_source=home_icon'
        ))

    def go_to_insurance_button_page(self):
        browser.should(have.url_containing(
            f'/insurance/?internal_source=home_icon'
        ))

    def go_to_travel_button_page(self):
        browser.should(have.url_containing(
            f'/travel/?internal_source=home_icon'
        ))
