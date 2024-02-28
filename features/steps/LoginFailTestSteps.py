import os

from behave import given, when, then
from appium import webdriver
from appium.options.common import AppiumOptions

# Import app screens
from screens.LoginPhoneScreen import LoginPhoneScreen
from screens.LoginCodeValidationScreen import LoginCodeValidationScreen


@given("James app is running")
def launch_app(context):
    context.driver = create_james_driver()
    context.driver.activate_app("com.hdw.james.rider")


@when("I enter a fake phone number \"{phone_number}\"")
def enter_phone_number(context, phone_number):
    login_screen = LoginPhoneScreen(context.driver)
    login_screen.enter_phone_number(phone_number)


@when("I tap \"Continue\" button on phone screen")
def tap_continue_button(context):
    login_screen = LoginPhoneScreen(context.driver)
    login_screen.tap_continue()


@then("I enter the invalid pin \"{pin_number}\"")
def enter_verification_code(context, pin_number):
    code_validation_screen = LoginCodeValidationScreen(context.driver)
    code_validation_screen.input_pin_individually(pin_number)


@when("I tap \"Continue\" on pin validation screen")
def tap_continue_button_on_code_screen(context):
    code_validation_screen = LoginCodeValidationScreen(context.driver)
    code_validation_screen.tap_continue()


@then("Login fails due to invalid credentials")
def verify_login_failure(context):
    # Check for error message on screen
    code_validation_screen = LoginCodeValidationScreen(context.driver)
    code_validation_screen.is_error_toast_displayed()
    kill_app("com.hdw.james.rider")
    context.driver.quit()


def create_james_driver():
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '13',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        'App': '/Users/darrencito/James Rider_1.22.0.apk',
        'AppPackage': 'com.hdw.james.rider',
    }

    james_driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(capabilities))
    return james_driver


def kill_app(package_name):
    os.system("adb shell am force-stop " + package_name)
