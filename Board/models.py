from django.db import models
from django.utils import timezone


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


class TeamPost(models.Model):
    parent = models.IntegerField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)


class TeamComment(models.Model):
    parent = models.IntegerField()
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)
    text = models.TextField()


class TeamLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class TeamPostFile(models.Model):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)
    file = models.FileField()