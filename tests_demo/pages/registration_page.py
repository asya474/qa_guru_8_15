from selene import have, command
from selene.support.shared import browser

import recources
from tests_demo.users.users import User


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_date_of_birth(self, user:User):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(user.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').send_keys(user.date_of_birth.year)
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.strftime("%d")}').click()

    def fill_state(self, user:User):
        browser.element('[id="state"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(user.state)).click()

    def fill_city(self, user:User):
        browser.element('[id="city"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(user.city)).click()

    def submit_form(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.number)
        self.fill_date_of_birth(user)
        browser.element('#subjectsInput').click().type(user.subject).press_enter()
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(user.hobbies)).click()
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(recources.path(user.image))
        browser.element('#currentAddress').type(user.address)
        self.fill_state(user)
        self.fill_city(user)
        browser.element('#submit').perform(command.js.click)

    def should_have_registrated_user(self, user:User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                f'{user.email}',
                f'{user.gender}',
                f'{user.number}',
                '{0} {1},{2}'.format(
            user.date_of_birth.strftime("%d"), user.date_of_birth.strftime("%B"), user.date_of_birth.strftime("%Y")),
                f'{user.subject}',
                f'{user.hobbies}',
                f'{user.image}',
                f'{user.address}',
                f'{user.state} {user.city}'
            )
        )