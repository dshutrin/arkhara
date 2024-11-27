from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('users/<int:uid>', user_detail)
]
