from django.urls import path
from ADMIN.views import *

app_name='ADMIN'

urlpatterns = [
    path('d/', index)
]
