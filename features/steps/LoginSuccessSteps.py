import os

from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Import app screens
from screens.LoginPhoneScreen import LoginPhoneScreen
from screens.LoginCodeValidationScreen import LoginCodeValidationScreen
from screens.JamesHomeScreen import JamesHomeScreen


@given("James app is open and running")
def launch_app(context):
    with create_james_driver() as context.james_driver:
        context.james_driver = create_james_driver()
        context.james_driver.activate_app("com.hdw.james.rider")


@when("I enter my phone number \"{phone_number}\"")
def enter_phone_number(context, phone_number):
    login_screen = LoginPhoneScreen(context.james_driver)
    login_screen.enter_phone_number(phone_number)


@when("I tap \"Continue\" on enter phone screen")
def phone_screen_tap_continue(context):
    login_screen = LoginPhoneScreen(context.james_driver)
    login_screen.tap_continue()
    context.james_driver.quit()


@then("I get the verification code from an SMS")
def get_verification_code(context):
    extracted_code = extract_james_code()
    if extracted_code:
        context.extracted_code = extracted_code  # Store code in context


@then("I enter the \"code\" on code screen")
def enter_verification_code(context):
    with create_james_driver() as context.james_driver:
        # Check if extracted code exists in context
        if hasattr(context, 'extracted_code'):
            code_validation_screen = LoginCodeValidationScreen(context.james_driver)
            code_validation_screen.input_pin_individually(context.extracted_code)

        else:

            print("Error: No verification code extracted.")


@when("I tap \"Continue\" on code screen")
def code_screen_tap_continue(context):
    with create_james_driver() as context.james_driver:
        code_validation_screen = LoginCodeValidationScreen(context.james_driver)
        code_validation_screen.tap_continue()


@then("I am logged into James app")
def verify_successful_login(context):
    with create_james_driver() as context.james_driver:
        james_home_screen = JamesHomeScreen(context.james_driver)
        james_home_screen.assert_home_menu_button()
        kill_app("com.hdw.james.rider")


def create_james_driver():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'platformVersion': '13',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        'App': '/Users/darrencito/James Rider_1.22.0.apk',
        'AppPackage': 'com.hdw.james.rider'
    }

    url = 'http://localhost:4723'
    james_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    return james_driver


def create_chrome_driver():

    chromedriver_path = ChromeDriverManager().install()

    cap = {
            'platformName': 'Android',
            'platformVersion': '13',
            'deviceName': 'emulator-5554',
            'automationName': 'UIAutomator2',
            'browserName': 'chrome',
            'chromedriverExecutable': chromedriver_path,
        }
    options = AppiumOptions().load_capabilities(cap)
    url = 'http://localhost:4723'

    # driver for Chrome website
    chrome_driver = webdriver.Remote(url, options=options)

    return chrome_driver


def extract_james_code():

    with create_chrome_driver() as chrome_driver:
        # Navigate to the website and interact with elements using Selenium methods
        chrome_driver.get("https://smstome.com/usa/phone/13022065094/sms/5924")

        # Implicit wait for website to load (optional)
        # chrome_driver.implicitly_wait(5)

        """Extracts the James code from the SMS message on the website.

        Args:
            driver: The Appium WebDriver object.

        Returns:
            The extracted James code, or None if not found.
        """

        for index in range(1, 6):  # Loop through potential message indexes
            xpath = f"//tbody/tr[{index}]/td[3]"
            try:
                element = chrome_driver.find_element(AppiumBy.XPATH, xpath)
                element_text = element.text

                if "Here is your James code:" in element_text:
                    code = element_text.split(": ")[-1]  # Extract code

                    if code:
                        print(f"Extracted James code: {code}")
                        return code

                    else:
                        print("James code not found in the SMS messages.")
                        return False

            except NoSuchElementException:
                pass  # Ignore exceptions for elements not found

        return None  # Return None if code not found within the loop


def kill_app(package_name):
    os.system("adb shell am force-stop " + package_name)