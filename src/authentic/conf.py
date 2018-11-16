""" Configuration variables used by Authentic """
import datetime


class AuthenticConfig:
    """ Default configurations for the Authentic application """

    # The default password rules for the application
    PASSWORD_RULES = {
        "min_length": 5,
        "max_length": 20,
        "upper_case": True,
        "lower_case": True,
        "digit": True,
        "max_invalid_attempts": 5,
        "min_topology_changes": 3,
        "blacklist": [
            "test",
            "Test",
            "Test@123"
        ]
    }

    # Default list of roles allowed for the application
    ROLES = ('ADMIN',)

    # Option to enable or disable account verifications
    ENABLE_VERIFICATION = False

    # Set the default authentication backend to Basic
    AUTHENTICATION_BACKEND = 'authentic.backends.basic'

    # JWT Backend related configuration
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=60)
    JWT_ALGORITHM = 'HS256'
    JWT_PRIVATE_KEY = None
    JWT_PUBLIC_KEY = None
    JWT_IDENTITY_CLAIM = 'identity'
    JWT_IDENTITY_CALLBACK = None
