import requests
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .forms import CityForm
from .models import City


def index(request):
    key = '7dea0aa06044cfb66e266c7462b623c8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=' + key

    # сохраняем город в БД
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    # очистка формы
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'name': city.name,
            'temp': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_city_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


# удаление города из БД
def del_city(request, id):
    try:
        City.objects.get(id=id).delete()
        return HttpResponseRedirect("/weather")
    except City.DoesNotExist:
        return HttpResponseNotFound("<h2>Город не найден</h2>")
