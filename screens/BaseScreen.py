from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseScreen:
    """
    Base class for all screen objects.
    Provides common functionality for interacting with elements.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    def find_element(self, locator_type, locator_value):
        """
        Finds an element on the page using the given locator.
        """
        return self.wait.until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )

    def click_element(self, locator_type, locator_value):
        """
        Clicks on an element on the page using the given locator.
        """
        self.find_element(locator_type, locator_value).click()

    def send_keys(self, locator_type, locator_value, text):
        """
        Sends text to an element on the page using the given locator.
        """
        self.find_element(locator_type, locator_value).send_keys(text)

    def is_element_present(self, locator_type, locator_value):
        """
        Checks if an element is present on the page using the given locator.
        """
        try:
            self.find_element(locator_type, locator_value)
            return True
        except Exception:
            return False
