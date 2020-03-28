from selenium import webdriver

class WebdriverFactory:

    def browserFactory(self, BrowserName):

        if BrowserName == 'firefox':
            return  webdriver.Firefox()

        elif (BrowserName == 'chrome'):
            return webdriver.Chrome(
                "C:/Users/ALL4TEST/PycharmProjects/frwPythonE2ETest/seleniumE2ETest/drivers/chromedriver.exe")

        elif BrowserName == 'opera':
            return webdriver.Opera()

        elif BrowserName == 'ie':
            return webdriver.Ie

        raise Exception("No such " + BrowserName + " browser exists")


