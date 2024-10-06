from django import forms
from django.core.exceptions import ValidationError
import calendar


class IsoToDate(forms.Form):
    VALUE_CHOICES = [(i, i) for i in range(1, 8)]  # Choices from 1 to 7
    year = forms.IntegerField(required=True, min_value=1)
    week = forms.IntegerField(required=True, min_value=1, max_value=53)
    day = forms.ChoiceField(required=True, choices=VALUE_CHOICES)
    # calc_type = forms.CharField(widget=forms.HiddenInput(), initial="iso_to_date")


class DateToIso(forms.Form):
    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]

    DAY_CHOICES = [(i, i) for i in range(1, 32)]

    year = forms.ChoiceField(choices=[(year, year) for year in range(1900, 2201)], label='Year')
    month = forms.ChoiceField(choices=MONTH_CHOICES, label='Month')
    day = forms.ChoiceField(choices=DAY_CHOICES, label='Day')
    # calc_type = forms.CharField(widget=forms.HiddenInput(), initial="date_to_iso")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     year = int(cleaned_data.get('year'))
    #     month = int(cleaned_data.get('month'))
    #     day = int(cleaned_data.get('day'))
    #
    #     # Check if the day is valid for the given month and year
    #     if day > calendar.monthrange(year, month)[1]:
    #         raise ValidationError(f'Day {day} is not valid for month {month} in year {year}.')

