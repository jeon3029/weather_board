from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
import requests
def index(request):
    return render(request, 'index.html')
    city = request.GET.get('city')
    # city = 'seoul'
    print(city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bc93e91cf9c28d68d266b93b2e7a46da'
    resp = requests.get(url=url,params=dict())
    data = resp.json()
    return JsonResponse(data)
    # return JsonResponse({'key':'value'})
