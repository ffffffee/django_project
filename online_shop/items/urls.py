from django.contrib import admin
from django.urls import include, path

from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('bytovaya-texnika',views.bytovaya_texnika,name="bytovaya-texnika"),
    path('smartfony-planshety-i-fototexnika',views.smartfony_planshety_i_fototexnika,name="smartfony-planshety-i-fototexnika"),
    path('tv-i-multimedia',views.tv_i_multimedia,name="tv-i-multimedia"),
    path('komplektuyushhie-kompyutery-i-noutbuki',views.komplektuyushhie_kompyutery_i_noutbuki,name="komplektuyushhie-kompyutery-i-noutbuki"),
    path('ofis-i-set',views.ofis_i_set,name="ofis-i-set"),
    path('otdyx-i-razvlecheniya',views.otdyx_i_razvlecheniya,name='otdyx-i-razvlecheniya'),
    path('instrumenty',views.instrumenty,name='instrumenty'),
    path('stroitelstvo-i-remont',views.stroitelstvo_i_remont,name='stroitelstvo-i-remont'),
    path('bytovaya-texnika/tehnika-for-kitchen',views.tehnika_for_kitchen,name="bytovaya-texnika"),
    path('bytovaya-texnika/tehnika-for-home',views.tehnika_for_home,name='tehnika_for_home')

]