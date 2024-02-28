from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class SignupEmailScreen(BaseScreen):

    """
    Represents the Email screen of the login/signup flow.
    Provides methods for interacting with login page elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

        self.email_screen_title = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/title")
        self.email_field = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/emailInput")
        self.continue_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/continueButton")

    def enter_email_address(self, email_address):
        """
        Enters email address
        """
        self.email_field.send_keys(email_address)

    def tap_continue(self):
        """
        Taps continue button on email address screen
        """
        self.continue_button.click()
