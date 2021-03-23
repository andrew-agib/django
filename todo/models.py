from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# class User(models.Model):
#   user_id = models.IntegerField(primary_key=True)
#  name = models.CharField(max_length=100)


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # finished = models.DateTimeField(auto_now=True)

    readonly_fields = ('created', 'finished')

    title = models.CharField(max_length=100, blank=False, default='')
    task_finished = models.BooleanField(default=False)
    description = models.CharField(max_length=100, blank=True, default='')

    choices = models.TextChoices('choices', 'programming bugfixing something')
    category = models.CharField(blank=True, choices=choices.choices, max_length=120)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user')
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user')

    # finished = models.DateTimeField(auto_now_add=False, blank=True)
    if task_finished is True:
        finished = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    else:
        finished = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Make sure this is the first save (pk should be None) and there is no unit_price set
        if self.task_finished is True:
            self.finished = str(datetime.now())
            # self.finished = models.DateTimeField(null=True, blank=True)

        #     self.finished = models.DateTimeField(auto_now=True, blank=True)
        #   self.finished = models.DateTimeField(auto_now_add=True, blank=True)
        # else:
        #   self.finished = models.DateTimeField(null=True, blank=True)

        #    self.finished=None
        #    self.finished = models.DateTimeField(auto_now_add=False, blank=True)

        super().save(*args, **kwargs)

    def __str__(self):
        if self.task_finished is True:
            return self.title + str(self.assigned) + str(self.task_finished)
        else:
            return self.title + str(self.assigned) + str(self.task_finished)
            # object.__str__(self)

# Create your models here.
