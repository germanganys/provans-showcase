from django.shortcuts import render


def error404_view(request, exception):
    return render(request, 'errors/404.html', {})


def error500_view(request):
    return render(request, 'errors/500.html', {})
