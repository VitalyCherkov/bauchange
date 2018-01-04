from django.shortcuts import render

def OK(request, **kwargs):
    return render(request, 'userprofile/settings.html')
