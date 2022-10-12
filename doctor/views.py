from django.shortcuts import render

# Create your views here.
def loginfun(request):
    return render(request,'doctor/login.html')


