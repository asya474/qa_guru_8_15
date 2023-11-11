import pytest
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach

def pytest_addoption(parser):
    parser.addoption('--remote_url', default='')

@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def browser_setup(request):
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
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    remote_url = request.config.getoption('--remote_url')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{remote_url}",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1200
    browser.config.window_width = 1600

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

#    yield

#    browser.quit()
