from django.shortcuts import render


# Display home page

def home(request):
    return render(request, 'home.html')

# 404 error handler

def handler404(request, exception):
    return render(request, '404.html', status=404)
