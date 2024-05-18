from django.shortcuts import render

def agregasi(input):
    result = input + 1
    return result

# Create your views here.
def page_landing(request):
    return render(request, 'app_landing/index.html')

def page_about(request):
    context = {
        'NAMA': 'daffa',
        'AGREGASI': agregasi(10)
    }
    return render(request, 'app_landing/about.html', context)

