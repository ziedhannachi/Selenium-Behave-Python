from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

class AuthentificationPageObject(object):
  __TIMEOUT = 10

  URL = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
  USERNAME_INPUT = (By.ID, 'txtUsername')
  PASSWORD_INPUT = (By.ID, 'txtPassword')
  LOGIN_BUTTON = (By.ID, 'btnLogin')

  def __init__(self, web_driver):
    self._web_driver_wait = WebDriverWait(web_driver, AuthentificationPageObject.__TIMEOUT)
    self._web_driver = web_driver

  def load(self):
    self._web_driver.get(self.URL)

  def usernameSendKeys(self, username):
    username_input = self._web_driver.find_element(*self.USERNAME_INPUT)
    username_input.send_keys(username)

  def passwordSendKeys(self, password):
      password_input = self._web_driver.find_element(*self.PASSWORD_INPUT)
      password_input.send_keys(password)

  def loginButtonClick(self):
      button_click = self._web_driver.find_element(*self.LOGIN_BUTTON)
      button_click.click()