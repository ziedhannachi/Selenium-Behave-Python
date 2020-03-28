from selenium import webdriver
from pagesOjects.AuthentificationPageObjects import AuthentificationPageObject
from Util.BrowserFactory import WebdriverFactory

webdriverFactory = WebdriverFactory()

def browser_chrome(context, timeout=30, **kwargs):

    browser = webdriverFactory.browserFactory('chrome')
    browser.maximize_window()

    authentification = AuthentificationPageObject(browser)
    context.authentification = authentification

    yield context.authentification
    browser.quit()