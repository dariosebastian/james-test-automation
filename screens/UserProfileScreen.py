from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from screens.BaseScreen import BaseScreen


class UserProfileScreen(BaseScreen):
    """
    Represents the Home screen of the James Rider app.
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.first_name_title = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/firstName")
        self.first_name_field = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/firstNameInput")
        self.done_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID")

    def assert_first_name_title(self):
        """
        Assert first name title is present on the screen
        """
        assert self.first_name_title.is_displayed()

    def change_first_name(self, first_name):
        """
        Change user's first name
        """
        self.first_name_field.send_keys(first_name)

    def tap_done(self):
        """
        Tap Done button to save changes
        """
        self.done_button.click()

    def is_success_toast_displayed(self):
        """
            Assert edit profile success toast is displayed with the expected message
        """
        try:
            success_toast = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/snackbar_text")

            # extract toast message text
            toast_message = success_toast.text

            # Verify if expected message matches exactly
            expected_message = "Profile updated successfully"
            assert toast_message == expected_message, f"Toast message doesn't match: {toast_message}"

        except TimeoutException:
            # Handle the case where the element is not found
            assert False, "Toast message element not found"
