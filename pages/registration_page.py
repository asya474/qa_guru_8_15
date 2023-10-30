from selene import have
from selene.support.shared import browser
import resources


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user):
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbie)).click()
        browser.element("#firstName").type(user.first_name)
        browser.element("#lastName").type(user.last_name)
        browser.element("#userEmail").type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element("#userNumber").type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month_of_birth)
        browser.element('.react-datepicker__year-select').type(user.year_of_birth)
        browser.element(f'.react-datepicker__day--0{user.day_of_birth}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('#uploadPicture').send_keys(resources.path(user.image))
        browser.element("#currentAddress").type(user.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()
        browser.element("#submit").click()

    def should_have_registered(self, user):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobbie,
            user.image,
            user.address,
            f'{user.state} {user.city}'
        ))
