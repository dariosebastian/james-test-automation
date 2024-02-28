import os

from behave import given, when, then
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions

# Import app screens
from screens.JamesHomeScreen import JamesHomeScreen
from screens.UserProfileScreen import UserProfileScreen
from screens.AccountScreen import AccountScreen


@given("James app is running with user already logged in")
def launch_app(context):
    with create_james_driver() as context.james_driver:
        context.james_driver = create_james_driver()
        context.james_driver.activate_app("com.hdw.james.rider")


@then("I tap on main menu button")
def open_main_menu(context):
    james_home_screen = JamesHomeScreen(context.james_driver)
    james_home_screen.tap_menu_button()


@when("I tap on the tile with users names")
def tap_user_profile_tile(context):
    account_screen = AccountScreen(context.james_driver)
    account_screen.tap_profile_name_tile()


@then("I am taken to the Profile screen")
def assert_profile_screen(context):
    profile_screen = UserProfileScreen(context.james_driver)
    profile_screen.assert_first_name_title()


@then("I change users first name to {first_name}")
def change_first_name(context, first_name):
    profile_screen = UserProfileScreen(context.james_driver)
    profile_screen.change_first_name(first_name)


@then("I tap Done button")
def tap_done_button_on_profile_screen(context):
    profile_screen = UserProfileScreen(context.james_driver)
    profile_screen.tap_done()


@then("Success toast message is displayed")
def verify_success_toast_displayed(context):
    profile_screen = UserProfileScreen(context.james_driver)
    profile_screen.is_success_toast_displayed()


@then("Account screen shows new name {new_name} on user profile tile")
def verify_new_name_is_displayed(context, new_name):
    account_screen = AccountScreen(context.james_driver)
    account_screen.assert_name_change(new_name)
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


def kill_app(package_name):
    os.system("adb shell am force-stop " + package_name)
