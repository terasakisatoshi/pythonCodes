#from django.shortcuts import render

from django.http import HttpResponse
from .models import AddWord
def index(request):
    data_list=AddWord.objects.all()
    return HttpResponse(data_list)
# Create your views here.
