from behave import *
from behave import given, when, then
import time


@given("I go to the application")
def step_impl(context):
    context.authentification.load()

@when('I enter "{username}" in the username field')
def step_impl(context, username):
    time.sleep(5)
    context.authentification.usernameSendKeys(username)


@step('I enter "{password}" in the password field')
def step_impl(context, password):
    time.sleep(5)
    context.authentification.passwordSendKeys(password)


@step("I press the login button")
def step_impl(context):
    time.sleep(5)
    context.authentification.loginButtonClick()


@then("The dashboard page is displayed")
def step_impl(context):
    time.sleep(5)


