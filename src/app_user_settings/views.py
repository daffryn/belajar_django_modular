from django.shortcuts import render

# Create your views here.
def page_user_settings(request):
    return render(request, 'app_user_settings/user_settings.html')

