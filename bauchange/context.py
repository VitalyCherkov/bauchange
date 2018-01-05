from userprofile.models import UserProfile


def current_userprofile(request):
    if hasattr(request, 'user') and request.user.is_authenticated():
        userprofile = UserProfile.objects.get(user=request.user)
    else:
        userprofile = None

    return {
        'context_userprofile': userprofile
    }