from django import path
from .views import *


urlpattern = [
    path('' ,home, name= 'home' )
]