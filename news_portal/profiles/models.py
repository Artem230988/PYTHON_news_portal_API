from django.db import models
from django.contrib.auth.models import AbstractUser
from dirtyfields import DirtyFieldsMixin
from news.utils import my_send_mail


class User(DirtyFieldsMixin, AbstractUser):
    is_banned = models.BooleanField(verbose_name='Заблокирован', default=False)

    def save(self, *args, **kwargs):
        if self.email:
            if self.is_dirty():
                dirty_fields = self.get_dirty_fields()
                if 'is_banned' in dirty_fields:
                    if self.is_banned == True:
                        my_send_mail('Ваш аккаунт заблокирован, теперь вы не можете оставлять комментарии',
                                     [self.email])
                    elif self.is_banned == False:
                        my_send_mail('Ваш аккаунт разблокирован, теперь вы можете оставлять комментарии',
                                     [self.email])
        super().save(*args, **kwargs)
