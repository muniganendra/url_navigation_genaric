from django.shortcuts import render

# Create your views here.
def muni(request):
    return render(request,'muni.html')

def yuva(request):
    return render(request,'yuva.html')