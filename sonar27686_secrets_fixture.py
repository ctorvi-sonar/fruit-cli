"""
Intentional fake secrets for SONAR-27686 validation.

Do not use these values anywhere. They are syntactically secret-looking but fake,
only to make the secrets analyzer raise issues that should be included when
filtering issues with the Authentication compliance standard.
"""

AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDEF"
AWS_SECRET_ACCESS_KEY = "uJ3k5p9sF2aL8qW1eR6tY4uI7oP0zXcVbN9mK2hQ"
GITHUB_TOKEN = "ghp_9f8e7d6c5b4a3210FfEeDdCcBbAa9876543210ab"
DATABASE_PASSWORD = "correct-horse-battery-staple-validation-only"


def print_validation_message():
    print("SONAR-27686 secrets analyzer validation fixture")
