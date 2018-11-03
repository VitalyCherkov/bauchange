from userprofile.models import UserProfile
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy


def current_userprofile(request):
    if hasattr(request, 'user') and request.user.is_authenticated:
        try:
            userprofile = UserProfile.objects.get(user=request.user)
        except:
            userprofile = None
    else:
        userprofile = None

    return {
        'context_userprofile': userprofile
    }


def menu_buttons(request):

    buttons = [
        {
            'label': _('Популярное'),
            'url': reverse_lazy('post:popular')
        },
        {
            'label': _('Новое'),
            'url': reverse_lazy('post:list')
        },
        {
            'label': _('Категории'),
            'url': reverse_lazy('category:all-categories')
        },
    ]

    return {
        'context_menu_buttons': buttons
    }