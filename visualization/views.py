from django.shortcuts import render

from visualization.tables import Linha as LinhaTable

def index(request):
    table = LinhaTable
    return render(request, "index.html", {'table': table})
