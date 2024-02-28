from behave.__main__ import main as behave_main

# List of feature file paths
feature_files = [
    "features/loginTestCase.feature",
    "features/editProfileTestCase.feature",
]

# Run Behave with the feature files
behave_main(feature_files)

print("All feature files executed successfully!")