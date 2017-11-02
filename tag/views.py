from django.shortcuts import render
from django.http import HttpResponse


def OK(request, **kwargs):
    return render(request, 'OK_user')