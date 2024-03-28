import random
import string

from django.http import HttpResponse
from django.shortcuts import render

import datetime
from .forms import *
from django.shortcuts import render

import matplotlib.pyplot as plt
import numpy as np


def intro(request):
    return HttpResponse("<center style=color:blue;>Welcome to TPM Homepage</center>")


def html(request):
    return render(request, 'newone.html')


def Homepage(request):
    return render(request, 'Homepage.html')


def Travelpackage(request):
    return render(request, 'Travelpackage.html')


def console(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['aditya']
        print(f'user_input:{user_input}')

    # return HttpResponse('Form submitted is successfully')
    out = {'user_input': user_input}
    return render(request, 'print_to_console.html', out)


def rando(request):
    return render(request, 'random123.html')


def random123(request):
    if request.method == "POST":
        in1 = request.POST['otp']
        in2 = int(in1)

    result = ''.join(random.sample(string.digits, in2))
    print(f'result:{result}')
    a2 = {'result': result}
    return render(request, "random123.html", a2)


def getdate_req(request):
    return render(request, 'getdate_template.html')


def getdate_template(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'getdate_template.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()

    return render(request, 'getdate_template.html', {'form': form})


def tzfunctioncall(request):
    return render(request, 'pytzexample.html')


def tzfunctionlogic(request):
    return render(request, 'pytzexample.html')


def registercall(request):
    return render(request, 'register.html')


from .models import *
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        # check if email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already exists choose a different email"
            # return HttpsResponse("email already registered choose a different email")
            return render(request, 'register.html', {'message1': message1})
        # create a new Register instance and save it
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('Homepage')
    return render(request, 'register.html')


def piechartcall(request):
    return render(request, 'pie_chart.html')


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'pie_chart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'pie_chart.html', {'form': form})


def photoslide(request):
    return render(request, 'photoslide.html')


def weathercall(request):
    return render(request, 'weather_input.html')


import requests


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '95b5e5c34bdde95b2ef64a683cd6efe7'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weather_input.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather_input.html', {'error_message': error_message})
