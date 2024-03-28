from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Home/', intro),
    path('html/', html, name='html'),
    path('', Homepage, name='Homepage'),
    path('Travel/', Travelpackage, name='Travelpackage'),
    path('c/', print_to_console, name='print_to_console'),
    path('console/', console, name='console'),
    path('ran1/', random123, name='random123'),
    path('random/', rando, name='rando'),
    path('date_request/', getdate_req, name='getdate_req'),
    path('getdate/', getdate_template, name='getdate_template'),
    path('tzcall/', tzfunctioncall, name="tzfunctioncall"),
    path('tzlogic/', tzfunctionlogic, name="tzfunctionlogic"),
    path('regicall/', registercall, name='registercall'),
    path('regilogin/', registerloginfunction, name="registerloginfunction"),
    path('piecall/', piechartcall, name='piechartcall'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('ps/', photoslide, name='photoslide'),
    path('wcall/', weathercall, name='weathercall'),
    path('wlogic/', weatherlogic, name='weatherlogic')
]
