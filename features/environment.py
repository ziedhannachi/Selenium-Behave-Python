from behave import use_fixture
from fixtures import browser_chrome
import traceback

def before_all(context):
    use_fixture(browser_chrome, context)