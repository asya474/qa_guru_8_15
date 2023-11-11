import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
    command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 412
    browser.config.window_height = 914
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

#@pytest.fixture(scope="function", autouse=True)
#def browser_management():
#    browser.config.window_width = 412
#    browser.config.window_height = 914
#    browser.config.base_url = "https://demoqa.com/automation-practice-form"
#    browser.config.timeout = 6.0

#    yield

#    browser.quit()
