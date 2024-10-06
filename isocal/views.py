from datetime import date
from django.shortcuts import render
from .forms import IsoToDate, DateToIso
import random
# Create your views here.


def iso_cal_home(request):
    try:
        today = date.today()
        date_iso = date.isocalendar(today)
        iso_to_date_form = IsoToDate(initial={'year': date_iso.year,
                                              'week': date_iso.week,
                                              'day': date_iso.weekday})
        result = ''
        # valid_keys = request.GET.keys()
        # 'year' in valid_keys and 'week' in valid_keys and 'day' in valid_keys:
        date_to_iso_form = DateToIso(initial={'year': today.year,
                                              'month': today.month,
                                              'day': today.day})
        result2 = ''
        exc = ''
        theme = request.session.get('theme', '')
        if request.method == 'POST':
            form = IsoToDate(request.POST)
            if form.is_valid():
                year = form.cleaned_data['year']
                week = form.cleaned_data['week']
                day = int(form.cleaned_data['day'])
                result = date.fromisocalendar(year=year, week=week, day=day)
                result = f'Year - {result.year}, Month - {result.month}, Day - {result.day}'
                iso_to_date_form = IsoToDate(initial={'year': year, 'week': week, 'day': day})
            else:
                form2 = DateToIso(request.POST)
                if form2.is_valid():
                    year = int(form2.cleaned_data['year'])
                    month = int(form2.cleaned_data['month'])
                    day = int(form2.cleaned_data['day'])
                    result2 = date.isocalendar(date(year, month, day))
                    result2 = f'Year - {result2.year}, Week - {result2.week}, Day - {result2.weekday}'
                    date_to_iso_form = DateToIso(initial={'year': year, 'month': month, 'day': day})
                else:
                    theme = random.choices(['basic.css', 'royal_purple.css',
                                            'berry-delight.css',
                                            'cool_grey.css', 'desert_sand.css',
                                            'earthy_tones.css', 'forest_green.css',
                                            'forest_whisper.css', 'froasted-ice.css',
                                            'midnight_blue.css', 'mint-chocolate.css',
                                            'ocean_blue.css', 'ocean_breeze.css', 'sunset_orange.css'])[0]
                    print("THEME", theme)
                    request.session['theme'] = theme

    except Exception as ex:
        print(ex)
        exc = str(ex)
        today = date.today()
        date_iso = date.isocalendar(today)
        iso_to_date_form = IsoToDate(initial={'year': date_iso.year,
                                              'week': date_iso.week,
                                              'day': date_iso.weekday})
        result = ''
        # valid_keys = request.GET.keys()
        # 'year' in valid_keys and 'week' in valid_keys and 'day' in valid_keys:
        date_to_iso_form = DateToIso(initial={'year': today.year,
                                              'month': today.month,
                                              'day': today.day})
        result2 = ''
        theme = request.session.get('theme', '')

    return render(request, 'isocal/home/home.html', {'form': iso_to_date_form,
                                                     'result': str(result),
                                                     'form2': date_to_iso_form,
                                                     'result2': str(result2),
                                                     'exception': exc,
                                                     'theme': theme})
