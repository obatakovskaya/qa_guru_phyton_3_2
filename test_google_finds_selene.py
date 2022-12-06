from _ast import Pass

from selene.support.shared import browser
from selene import have, be


def test_g_finds(open_browser):
    browser.element('[name=q][type="text"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_g_findes2(open_browser):
    browser.element('[name=q][type="text"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('dsfsdfsdfsdfsf'))
