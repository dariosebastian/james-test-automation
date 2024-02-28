# james-test-automation
James App test automation v0.0.1

#### _Tech stack:_
- Python v3.12.0
- Behave v1.2.6
- Appium v2.5.1

### Steps to run the Test Plan including all Features:

**Install tools/dependencies (if not available yet)**

Appium v2.5.1: `npm install -g appium`

Behave v1.2.6: `pip install behave`

1. **Clone repo:**
`https://github.com/dariosebastian/james-test-automation.git`


2. **Have an android emulator running on Android Studio:** suggested device API 33


3. Setup Appium capabilites on Driver creation to match your emulator location:


    'platformName': 'Android'
    'platformVersion': '13',
    **'deviceName': 'your_device_name',** (usually emulator-5554)
    'automationName': 'UIAutomator2',
    **'App': '/your_path_to_app_apk/James Rider_1.22.0.apk',**
    'AppPackage': 'com.hdw.james.rider',`

### **IMPORTANT NOTE:** 
Since 'environment.py' is not yet setup completely, you will need to update the capabilites on each steps file, as follows:
- features/steps/EditProfileTestSteps.py
- features/steps/LoginFailTestSteps.py
- features/steps/LoginSuccessSteps.py
- features/steps/SignupSuccessTestSteps.py

4. On a terminal window, run Appium server.

4. **On a new terminal window, activate virtual environment:**
`source /path/to/your/virtualenv/bin/activate`

_generally path will be:_ ~/your_clone_destination_folder/james-test-automation/.venv/bin/activate


5. **And finally run test plan .py script:** This will execute all features and provide a final report after execution.

`Python RunTestPlan.py`

6. After execution is completed, you can find a full HTML report on the project root folder.


**Known Issues:**

- SignUpTestCase.feature is left out of the test plan since it is unfinished.
- Proper handling of @after_scenarios is not yet developed, so in case a failure occurs, test plan will likely be interrupted.
- After execution is finished, you will need to manually 'Sign out' of the app to repeat the test, since logout flow is not yet automated.