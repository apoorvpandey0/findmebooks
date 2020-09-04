from django.db import models
from django.utils.translation import gettext as _

from users.models import Profile

STATUS_CHOICES = (
    (1,'For sale'),
    (2,'For rent'),
    (3,'Giveaway'),
)

class UserBook(models.Model):
    user = models.ForeignKey(Profile,on_delete = models.SET_NULL,null=True)
    isbn   = models.CharField(max_length=13)
    status = models.IntegerField(choices = STATUS_CHOICES,null=True)
    image          = models.ImageField(
                        _('Book Image'),
                        default='default.png',
                        upload_to='book_images',
                        help_text=_('Designates the users book images.')
    )

