from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class JamesHomeScreen(BaseScreen):
    """
    Represents the Home screen of the James Rider app.
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.menu_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/MAIN_MENU_ID")

    def assert_home_menu_button(self):
        """
        Check Home menu button is displayed
        """
        assert self.menu_button.is_displayed()

    def tap_menu_button(self):
        """
        Check Home menu button is displayed
        """
        self.menu_button.click()
