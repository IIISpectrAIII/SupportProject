from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    STATUS = (
        (1, 'Done'),
        (2, 'Not done'),
        (3, 'Frozen')
    )

    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    issue = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    status = models.PositiveSmallIntegerField(choices=STATUS, default="2")

    def __str__(self):
        return f'{self.username}: {self.issue}. {self.status}'


class Comment(models.Model):
    """Ответы на Ticket"""
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.user} \n {self.text}'
