from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
import requests
def index(request):
    return render(request, 'index2.html')
    city = request.GET.get('city')
    # city = 'seoul'
    print(city)
