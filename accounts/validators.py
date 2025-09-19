import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class StandardPasswordValidator:
    def validate(self, password: str, user=None):
        if not re.search(r'\d', password):
            raise ValidationError(
                _("Your password has no numbers."),
                code='password_no_number',
            )
        
        if not re.search(r'[a-zA-Z]', password):
            raise ValidationError(
                _("Your password has no letters."),
                code='password_no_letter',
            )
        
        if not re.search('[!@#$%^&*()_+\\-=\\[\\]{};\':"\\\\|,.<>\\/?]', password):
            raise ValidationError(
                _("Your password has no special characters."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _("Your password must include numbers, letters, and special characters at once.")

    def __call__(self, password: str, user=None):
        return self.validate(password, user)