from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime, date, timedelta

def validate_even(value):
    if value == emp_days_off:
        raise ValidationError(
            _('nope!'),
            params={'value': value},
        )


def validate_time_request(self):
    day_passed = self.cleaned_data.get("not_available")
    today = date.today()
    notice = timedelta(days=14)
    if day_passed <= (today + notice):
        print("can't request off")
        raise ValidationError("Request must be made two weeks in advance.")
    return day_passed
