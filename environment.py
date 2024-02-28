from appium import webdriver
from appium.options.common import AppiumOptions

capabilities = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'emulator-5554',
    'automationName': 'UIAutomator2',
    'App': '/Users/darrencito/James Rider_1.22.0.apk',
    'AppPackage': 'com.hdw.james.rider',
}


def before_all(context):
    """
    Creates and initializes the Appium driver before each test execution.
    """
    options = AppiumOptions().load_capabilities(capabilities)
    context.driver = webdriver.Remote('http://localhost:4723', options=options)


def after_scenario(context, scenario):
    """
    Quits the Appium driver after each scenario to terminate the app.
    """
    context.driver.quit()
