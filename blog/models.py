import itertools
from django.db import models
from comments.models import Comment
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify


class Post(models.Model):
    """  Model representation of the Post """

    title = models.CharField(_('Post Title'), max_length=150, unique=True)
    slug = models.SlugField(_('Slug'), max_length=150, unique=True)
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

    def generate_slug(self):
        """ Generate & return a unique slug """ 

        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Post.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self.generate_slug()

        super().save(*args, **kwargs)
