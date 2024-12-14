from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')

def maintenance(request):
    return render(request, 'maintenance.html')

def repair(request):
    return render(request, 'repair.html')

def price(request):
    return render(request, 'price.html')

def locations(request):
    return render(request, 'locations.html')