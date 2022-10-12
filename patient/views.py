from django.shortcuts import render

# Create your views here.
def slotefun(request):
    return render(request,'patient/booking.html')
    