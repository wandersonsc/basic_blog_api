from django.db import models
from comments.models import Comment
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    """  Model representation of the Post  """

    title = models.CharField(_('Post Title'), max_length=200, unique=True)
    comments = models.ForeignKey(Comment, related_name='Comments', on_delete=models.CASCADE)
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = "My Post"
        verbose_name_plural = "My Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})
