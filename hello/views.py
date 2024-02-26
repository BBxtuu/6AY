from django.shortcuts import render
from datetime import datetime
import re
import random


def hello(request):
    return render(request, 'hello/hello_template.html', {})

def it_is_me(request):
    return render(request, 'hello/hello_template.html', {})

def format_date(date, euro=True):
    if euro:
        return date.strftime("%d. %B %Y, currently the time is: %X.")   #europäische
    else:
        return date.strftime("%m/%d/%Y, currently the time is: %X.")    #amerikanisch

def hello_there(request, name):
    now = datetime.now()
    euro = random.choice([True, False])  
    formatted_now = format_date(now, euro)

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    context = {
        'clean_name': clean_name,
        'formatted_now': formatted_now,
    }

    return render(request, 'hello/hello_template.html', context)
