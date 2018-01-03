from django.db import models, IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django import forms
from .models import Post
from tag.models import Tag
from userprofile.models import UserProfile


class CreatePostForm(forms.ModelForm):

    tags = forms.CharField(max_length=250)
    tags.label = 'Теги'
    tags.help_text = 'Введите через пробел не более трех тэгов.'

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'category': 'Категория'
        }

        help_texts = {
            'title': 'Максимальная длина - 250 символов.'
        }

    def clean(self):
        cleaned_data = super(CreatePostForm, self).clean()
        return cleaned_data

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        tags = tags.split()
        if len(tags) > 3:
            raise forms.ValidationError(
                _("Должно быть не более трех тегов."),
                code='count'
            )

        tag_max_len = Tag._meta.get_field('label').max_length
        for tag in tags:

            if len(tag) > tag_max_len:
                raise forms.ValidationError(
                    _("Максимальная длина тега не должна превышать %(value)d символов."),
                    code='tag_length',
                    params={'value': tag_max_len}
                )

        return tags

    def save(self):
        post = Post()
        post.title = self.cleaned_data['title']
        post.text = self.cleaned_data['text']
        post.category = self.cleaned_data['category']
        post.author = self.author
        post.save()

        for tag_ in self.cleaned_data['tags']:
            try:
                post.tag.create(label=tag_)
            except IntegrityError:
                post.tag.add(Tag.objects.get(label=tag_))

        return post

    def set_user(self, user):
        self.author = UserProfile.objects.get(user=user)



