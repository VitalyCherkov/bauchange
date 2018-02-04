from rest_framework import serializers
from userprofile.models import UserProfile


class UserProfileShortSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = ('url', 'first_name', 'last_name')
        extra_kwargs = {
            'url': {'view_name': 'userprofile:userpage', 'lookup_field': 'pk'}
        }