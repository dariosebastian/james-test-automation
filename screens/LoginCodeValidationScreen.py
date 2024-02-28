from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from screens.BaseScreen import BaseScreen


class LoginCodeValidationScreen(BaseScreen):
    """
    Represents the code validation screen of the James Rider app.
    Provides methods for interacting with code validation page elements.
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.error_toast = None
        self.codeScreenTitle = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/title")
        self.pinCodeField = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/inputContainer")
        self.continue_button = self.find_element(AppiumBy.ID, "com.hdw.james.rider:id/continueButton")
        self.pin_fields = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText["
                                                                    "@resource-id='com.hdw.james.rider:id"
                                                                    "/inputEditText']")

    def input_pin_individually(self, pin_number):
        pin_number_str = str(pin_number)  # Convert PIN to string
        for i in range(len(pin_number_str)):
            digit = pin_number_str[i]
            pin_field = self.pin_fields[i]  # Access the corresponding PIN field
            pin_field.click()  # Focus on the field
            pin_field.send_keys(digit)  # Send the digit

    def tap_continue(self):
        """
                Taps continue button on code validation screen
                """
        self.continue_button.click()

    def is_error_toast_displayed(self):
        """
            Assert error toast is displayed with the expected message
        """
        try:
            error_toast = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.hdw.james.rider:id/snackbar_text"))
            )
            # extract error toast text
            toast_message = error_toast.text

            # Verify if expected message matches exactly
            expected_message = "Invalid credentials"
            assert toast_message == expected_message, f"Error message doesn't match: {toast_message}"

        except TimeoutException:
            # Handle the case where the element is not found
            assert False, "Error message element not found"

