from django.shortcuts import render


def index(request):
    data = {
        'titel': 'Главная страница!',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def cont(request):
    return render(request, 'main/cont.html')


# Create your views here.
