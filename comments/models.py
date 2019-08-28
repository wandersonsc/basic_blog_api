from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    """  Model representation of the Comment  """

    comments = models.TextField(_('Comments'))
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name: "My Comment"
        verbose_name_plural: "My Comments"

    def __str__(self):
        return self.comments

    # def get_absolute_url(self):
    #     return reverse('post:detail', kwargs={'pk': self.pk})
