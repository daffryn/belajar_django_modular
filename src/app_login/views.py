from django.shortcuts import render

# Create your views here.
def page_login(request):
    return render(request, 'app_login/login.html')

