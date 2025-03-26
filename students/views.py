from django.shortcuts import render
from django.http import HttpResponce


def example_view(request):
    return render(request, 'app/example.html')


def show_data(request):
    if request.method == 'GET':
        return render(request, 'app/show_data.html')


def submit_data(request):
    if request.method == 'POST':
        return HttpResponce('Данные отправлены')
