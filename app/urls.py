from django.urls import path
from .views import home, login, contacto, arriendo, hotel, tour, quienes_somos, registro

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('contacto/', contacto, name="contacto"),
    path('arriendo/', arriendo, name="arriendo"),
    path('hotel/', hotel, name="hotel"),
    path('tour/', tour, name="tour"),
    path('quienes-somos/', quienes_somos, name="quienessomos"),
    path('registro/', registro, name="registro"),
]