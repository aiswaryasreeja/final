from django.shortcuts import render

def home(request):
    return render(request, 'hey.html')

# You can define more views for different sections of your website
