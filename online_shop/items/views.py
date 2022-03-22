from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
def main_page(request):
    return HttpResponse(render_to_string('items/main_page.html'))
def bytovaya_texnika(request):
    return HttpResponse(render_to_string('items/bytovaya_texnika.html'))
def smartfony_planshety_i_fototexnika(request):
    return HttpResponse(render_to_string('items/smartphones_and_gadgets.html'))
def tv_i_multimedia(request):
    return HttpResponse(render_to_string('items/tv_and_multimedia.html'))
def komplektuyushhie_kompyutery_i_noutbuki(request):
    return HttpResponse(render_to_string('items/computers.html'))
def ofis_i_set(request):
    return HttpResponse(render_to_string('items/office_and_set.html'))
def otdyx_i_razvlecheniya(request):
    return HttpResponse(render_to_string('items/otdyh_and_entertainment.html'))
def instrumenty(request):
    return HttpResponse(render_to_string('items/instruments.html'))
def stroitelstvo_i_remont(request):
    return HttpResponse(render_to_string('items/stroyka_and_remont.html'))
def tehnika_for_kitchen(request):
    data = {
        'link': 'http://127.0.0.1:8000/dns/bytovaya-texnika/tehnika-for-kitchen',
        'cat1':'Приготовление пищи',
        'cat2':'Приготовление напитков',
        'cat3':'Холодное оборудование',
        'cat4':'Посудомоечные машины',
        'cat5': 'Приготовление десертов',
        'cat6': 'Измерения',
        'cat7': 'Нарезка, смешивание, упаковка',
        'cat8': 'Прочие товары для кухни',
        'link_img1':"img/1554190.png",
        'link_img2':"img/491558.png",
        'link_img3':"img/395547.png",
        'link_img4':"img/3321605.png",
        'link_img5':"img/294653.png",
        'link_img6':"img/2928937.png",
        'link_img7':"img/2245002.png",
        'link_img8':"img/3728210.png",
    }
    return render(request, 'items/template_for_categories.html', data)
def tehnika_for_home(request):
    data={
        'link': 'http://127.0.0.1:8000/dns/bytovaya-texnika/tehnika-for-home',
        'cat1':'Стирка и сушка',
        'cat2':'Глаженье',
        'cat3':'Уборка',
        'cat4':'Летний климат',
        'cat5': 'Шитье, вышивание и уход за одеждой',
        'cat6': 'Умный дом',
        'cat7': 'Поддержание климата',
        'cat8': 'Часы',
        'link_img1':"img/3322056.png",
        'link_img2':"img/698644.png",
        'link_img3':"img/2829843.png",
        'link_img4':"img/1135215.png",
        'link_img5':"img/2175738.png",
        'link_img6':"img/1384521.png",
        'link_img7':"img/2482799.png",
        'link_img8':"img/2784399.png",
    }
    return render(request,'items/template_for_categories.html',data)
def beauty_and_health(request):
    data = {
        'link': 'http://127.0.0.1:8000/dns/bytovaya-texnika/beauty-and-health',
        'cat1': 'Укладка и сушка волос',
        'cat2': 'Бритье и эпиляция',
        'cat3': 'Стрижка волос',
        'cat4': 'Профессиональная техника',
        'cat5': 'Шитье, вышивание и уход за одеждой',
        'cat6': 'Умный дом',
        'cat7': 'Поддержание климата',
        'cat8': 'Часы',
        'link_img1': "img/3322056.png",
        'link_img2': "img/698644.png",
        'link_img3': "img/2829843.png",
        'link_img4': "img/1135215.png",
        'link_img5': "img/2175738.png",
        'link_img6': "img/1384521.png",
        'link_img7': "img/2482799.png",
        'link_img8': "img/2784399.png",
    }
    return render(request, 'items/template_for_categories.html', data)