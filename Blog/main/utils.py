from django.contrib.auth.password_validation import MinimumLengthValidator

class MinimumLengthValidatorSix(MinimumLengthValidator):
    def __init__(self, min_length: int = 6) -> None:
        super().__init__(min_length)