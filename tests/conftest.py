import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_manage():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1100
    browser.config.window_height = 2300

    yield

    browser.quit()
