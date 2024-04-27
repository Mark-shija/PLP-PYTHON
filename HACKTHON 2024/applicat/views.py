from django.shortcuts import render
import requests

API_KEY = 'd46ffe39415f4c46bb01bfd69bc07ba6'


def index(request):
    # News API 
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}')
        data = response.json()
        articles = data['articles']
    else:
        response = requests.get(f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}')
        data = response.json()
        articles = data['articles']


    context = {
        'articles': articles,

    }  
    return render(request, "templates/index.html", context)


