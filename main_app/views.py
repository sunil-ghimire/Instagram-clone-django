from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')

def profile(request):
    return render(request, 'homepage/profile.html')