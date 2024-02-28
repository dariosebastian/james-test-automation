from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class LoginPhoneScreen(BaseScreen):

    """
    Represents the login screen of the James Rider app.
    Provides methods for interacting with login page elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

        self.phone_field = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/input")
        self.continue_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/continueButton")

    def enter_phone_number(self, phone_number):
        """
        Enters phone number
        """
        self.phone_field.send_keys(phone_number)

    def tap_continue(self):
        """
        Taps continue button on phone number screen
        """
        self.continue_button.click()
