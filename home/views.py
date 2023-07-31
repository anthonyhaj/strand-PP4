from django.shortcuts import render

# Display home page

def home(request):
    return render(request, 'home/home.html')
