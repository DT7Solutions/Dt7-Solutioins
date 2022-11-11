from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'uifiles/home.html')

def about(request):
    return render (request, 'uifiles/about.html')

def services(request):
    return render (request, 'uifiles/service.html')

def blog(request):
    return render (request, 'uifiles/blog.html')

def careers(request):
    return render (request, 'uifiles/careers.html')

def contact(request):
    return render (request, 'uifiles/contact.html')

