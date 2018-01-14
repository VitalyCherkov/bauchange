from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateCommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = [
            'text'
        ]

    def save(self, commit=True):
        comment = Comment(author=self.request.user)