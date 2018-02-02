from django.db import models
from django.utils import timezone
from Profile.models import UserInfo


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


class Post(models.Model):
    writer = models.ForeignKey(UserInfo, default='', on_delete=models.SET_DEFAULT)
    parent = models.IntegerField(default=-1)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    file = models.FileField()

    class Meta:
        abstract = True


class Comment(models.Model):
    parent = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        abstract = True


class PostLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TeamPost(Post):
    file = models.FileField(upload_to='static/file/team')


class TeamComment(Comment):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class TeamLabel(PostLabel):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class PedigreePost(Post):
    file = models.FileField(upload_to='static/file/pedigree')


class PedigreeComment(Comment):
    post = models.ForeignKey(PedigreePost, on_delete=models.CASCADE)


class PedigreeLabel(PostLabel):
    post = models.ForeignKey(PedigreePost, on_delete=models.CASCADE)


class GreetingsPost(Post):
    file = models.FileField(upload_to='static/file/greetings')


class GreetingsComment(Comment):
    post = models.ForeignKey(GreetingsPost, on_delete=models.CASCADE)


class GreetingsLabel(PostLabel):
    post = models.ForeignKey(GreetingsPost, on_delete=models.CASCADE)


class ShareInfoPost(Post):
    file = models.FileField(upload_to='static/file/share_info')


class ShareInfoComment(Comment):
    post = models.ForeignKey(ShareInfoPost, on_delete=models.CASCADE)


class ShareInfoLabel(PostLabel):
    post = models.ForeignKey(ShareInfoPost, on_delete=models.CASCADE)


class ANTAlgorithmPost(Post):
    file = models.FileField(upload_to='static/file/ant_algorithm')


class ANTAlgorithmComment(Comment):
    post = models.ForeignKey(ANTAlgorithmPost, on_delete=models.CASCADE)


class ANTAlgorithmLabel(PostLabel):
    post = models.ForeignKey(ANTAlgorithmPost, on_delete=models.CASCADE)


class CompetitionPost(Post):
    file = models.FileField(upload_to='static/file/competition_algorithm')


class CompetitionComment(Comment):
    post = models.ForeignKey(CompetitionPost, on_delete=models.CASCADE)


class CompetitionLabel(PostLabel):
    post = models.ForeignKey(CompetitionPost, on_delete=models.CASCADE)

