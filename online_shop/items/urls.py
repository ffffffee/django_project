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
    path('bytovaya-texnika/tehnika-for-home',views.tehnika_for_home,name='tehnika_for_home'),
    path('bytovaya-texnika/beauty-and-health',views.beauty_and_health,name='beauty_and_health'),
    path('smartfony-planshety-i-fototexnika/smartfony-i-gadzhety',views.smartphones_and_gadgets,name="smartfony_i_gadzhety"),
    path('smartfony-planshety-i-fototexnika/ebooks-and-tablets',views.ebooks_and_tablets,name='ebooks_and_tablets'),
    path('registration',views.add_user,name="add_user"),
    path('add-item',views.add_item,name="add_item"),
    path('add-produser',views.add_produser,name="add_produser"),
    path('bytovaya-texnika/tehnika-for-kitchen/cooking-dishes/',views.page_of_items,name="page_of_items"),
    path('bytovaya-texnika/tehnika-for-kitchen/cooking-dishes/<slug:slug>/',views.ItemDetailView.as_view(), name='item-detail')
]