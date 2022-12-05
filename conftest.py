import pytest
from selene.support.shared import browser
from selene import have, be


@pytest.fixture(scope='session')
def open_browser():
    browser.open('https://www.google.com/ncr').driver.maximize_window()
    yield
    browser.close()


