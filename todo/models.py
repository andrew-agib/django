from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Task(models.Model):
    readonly_fields = ('created_at', 'finished_at')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    task_finished = models.BooleanField(default=False)
    description = models.CharField(max_length=100, blank=True, default='')
    choices = models.TextChoices('choices', 'programming bugfix something')
    category = models.CharField(blank=True, choices=choices.choices, max_length=120)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_user')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user')
    finished_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.task_finished is True:
            self.finished_at = str(timezone.now())
        super().save(*args, **kwargs)

    def __str__(self):
        if self.task_finished is True:
            return self.title + " " + str(self.assigned_to) + " " + str(self.task_finished)
        else:
            return self.title + " " + str(self.assigned_to) + " " + str(self.task_finished)
