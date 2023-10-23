from django.urls import path
from .views import *

urlpatterns = [
    path('', api_view, name="api_view"),
    #path('<int:pk>', DetailApiControle.as_view())
]
