from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня полчилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')
