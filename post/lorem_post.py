from random import randint
from .models import Post
from category.models import Category
from comment.models import Comment
from userprofile.models import User
from tag.models import Tag
from faker import lorem


def get_lorem_post():
    post = Post(
        title=lorem.sentence(randint(1, 5)),
        text=lorem.paragraphs(randint(1, 5)),
        likes=randint(3, 8),
        dislikes=randint(1, 5),
        views=randint(15, 30),
        category=Category.objects.get(pk=1),
        user=Category.objects.get(pk=1)
    )
    # post.tag = Tag.objects.all(),
    return post
