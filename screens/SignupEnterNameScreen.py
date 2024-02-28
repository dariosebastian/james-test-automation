from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class SignupEnterNameScreen(BaseScreen):

    """
    Represents the Enter name of the signup flow.
    Provides methods for interacting with login flow elements.
    """
    def __init__(self, driver):
        super().__init__(driver)

        self.name_screen_title = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/textTitle")
        self.first_name_field = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/firstNameInput")
        self.last_name_field = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/lastNameInput")
        self.continue_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/buttonContinue")

    def enter_first_name(self, first_name):
        """
        Enters user's first name
        """
        self.first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enters user's last name
        """
        self.last_name_field.send_keys(last_name)

    def tap_continue(self):
        """
        Taps continue button on enter name screen
        """
        self.continue_button.click()
