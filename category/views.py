from django.shortcuts import render
from django.http import HttpResponse

def foo(request):
    return render(request, 'base.html', {
        'title' : 'CATEGORY!',
        'text' : 'category content',
    })

    return HttpResponse('Category!')
