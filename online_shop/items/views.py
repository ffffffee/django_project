from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .forms import AddUserForm,AddItemForm,AddProduser
from .models import Items
from django.views.generic import DetailView

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
        'title':"Техника для кухни",
        'link1': 'http://127.0.0.1:8000/bytovaya-texnika/tehnika-for-kitchen/cooking-dishes/',
        'cat1': 'Приготовление пищи',
        'cat2': 'Приготовление напитков',
        'cat3': 'Холодное оборудование',
        'cat4': 'Посудомоечные машины',
        'cat5': 'Приготовление десертов',
        'cat6': 'Измерения',
        'cat7': 'Нарезка, смешивание, упаковка',
        'cat8': 'Прочие товары для кухни',
        'link_img1': "img/1554190.png",
        'link_img2': "img/491558.png",
        'link_img3': "img/395547.png",
        'link_img4': "img/3321605.png",
        'link_img5': "img/294653.png",
        'link_img6': "img/2928937.png",
        'link_img7': "img/2245002.png",
        'link_img8': "img/3728210.png",
    }
    return render(request, 'items/template_for_categories.html', data)


def tehnika_for_home(request):
    data = {
        "title":"Техника для дома",
        'link': 'http://127.0.0.1:8000/bytovaya-texnika/tehnika-for-home',
        'cat1': 'Стирка и сушка',
        'cat2': 'Глаженье',
        'cat3': 'Уборка',
        'cat4': 'Летний климат',
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


def beauty_and_health(request):
    data = {
        'title':'Красота и здоровье',
        'link': 'http://127.0.0.1:8000/bytovaya-texnika/beauty-and-health',
        'cat1': 'Укладка и сушка волос',
        'cat2': 'Бритье и эпиляция',
        'cat3': 'Стрижка волос',
        'cat4': 'Профессиональная техника',
        'cat5': 'Здоровье',
        'cat6': 'Маникюр и педикюр',
        'cat7': 'Уход за полостью рта',
        'cat8': 'Массаж',
        'link_img1': "img/2792633.png",
        'link_img2': "img/682608.png",
        'link_img3': "img/3461768.png",
        'link_img4': "img/1658253.png",
        'link_img5': "img/4521426.png",
        'link_img6': "img/2444753.png",
        'link_img7': "img/6212141.png",
        'link_img8': "img/5606912.png",
    }
    return render(request, 'items/template_for_categories.html', data)


def smartphones_and_gadgets(request):
    data = {
        'title':'Смартфоны и гаджеты',
        'link': 'http://127.0.0.1:8000/bytovaya-texnika/smartphones_and_gadgets',
        'cat1': 'Смартфоны',
        'cat2': 'Смарт-часы и браслеты',
        'cat3': 'Сотовый телефон',
        'cat4': 'Детские часы',
        'cat5': 'Аксессуары для смарт-часов и браслетов ',
        'cat6': 'Стационарные сотовые телефоны',
        'cat7': 'Аксессуары для смартфонов',
        'cat8': 'Радиостанции',
        'link_img1': "img/186239.png",
        'link_img2': "img/617690.png",
        'link_img3': "img/111112.jpg",
        'link_img4': "img/111113.jpg",
        'link_img5': "img/111114.jpg",
        'link_img6': "img/111115.jpg",
        'link_img7': "img/111116.jpg",
        'link_img8': "img/111117.jpg",
    }
    return render(request, 'items/template_for_categories.html', data)

def ebooks_and_tablets(request):
    data = {
        'title':'Планшеты и электронные книги',
        'link': 'http://127.0.0.1:8000/smartfony-planshety-i-fototexnika/ebooks-and-tablets',
        'cat1': 'Планшеты',
        'cat2': 'Электронные книги',
        'cat3': 'Цифровые блокноты',
        'cat4': 'Аксессуары для планшетов',
        'cat5': 'Чехлы для электронных книг',
        'cat6': 'Тарифы операторов',

        'link_img1': "img/644476.png",
        'link_img2': "img/3211286.png",
        'link_img3': "img/111112.jpg",
        'link_img4': "img/111113.jpg",
        'link_img5': "img/111114.jpg",
        'link_img6': "img/111115.jpg",

    }
    return render(request, 'items/1.html', data)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AddUserForm()

    return render(request, 'items/registration_form.html', {'form': form})

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = AddItemForm()

    return render(request, 'items/add_item.html', {'form': form})

def add_produser(request):
    if request.method == 'POST':
        form = AddProduser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = AddProduser()

    return render(request, 'items/add_produser.html', {'form': form})

def page_of_items(request):
    items=Items.objects.all()

    return render(request,'items/page_of_items.html',{'items':items,'link_img1': "img/111111.jpg"})

class ItemDetailView(DetailView):
    model=Items
    template_name='items/item_template.html'
    context_object_name = "item"