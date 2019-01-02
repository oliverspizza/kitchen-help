from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value == emp_days_off:
        raise ValidationError(
            _('nope!'),
            params={'value': value},
        )
