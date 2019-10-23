from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    """  Model representation of the Comment  """

    comments = models.TextField(_('Comments'), help_text="Comments goes here")
    create_at = models.DateTimeField(_('Create at'), 
    auto_now_add=True,
    help_text="Create at"
    )
    updated_at = models.DateTimeField(_('Updated at'), 
    auto_now=True,
    help_text="Updating data"
    )
    status = models.BooleanField(_('Approved comment'), 
    default = False,
    help_text="Switch between approved comments"
    )

    class Meta:
        verbose_name = "My Comment"
        verbose_name_plural = "My Comments"

    def __str__(self):
        return self.comments

    def approve(self):
        self.status=True
        self.save()
    # def get_absolute_url(self):
    #     return reverse('post:detail', kwargs={'pk': self.pk})
