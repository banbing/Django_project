from django.shortcuts import render, HttpResponse
from app01 import models
from app01.tables import DataInfotable

# Create your views here.


def index(request):
    if request.method == 'GET':
        data = models.DataInfo.objects.all()
        return render(request, 'index.html', {"data": data})
    return HttpResponse('ok')