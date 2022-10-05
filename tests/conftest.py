import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='100.0')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', params=[('1920', '1080'), ('1600', '900')])
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)
    # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    browser.config.driver = driver
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function', params=[('750', '1334')])
def setup_mobile_browser(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)
    # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    browser.config.driver = driver
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)
    browser.quit()
