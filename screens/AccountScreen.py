from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class AccountScreen(BaseScreen):
    """
    Represents the Main Menu screen of the James Rider app.
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.profile_name_tile = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/profileName")

    def tap_profile_name_tile(self):
        """
        Tap profile name tile
        """
        self.profile_name_tile.click()

    def assert_name_change(self, new_name):
        """
        Assert that the profile name tile displays the new first name.
        """
        full_name_text = self.profile_name_tile.text
        assert new_name in full_name_text, f"New first name '{new_name}' not found in profile name: {full_name_text}"
