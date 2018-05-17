import os
from django.db import models
from django.utils import timezone

from ANTCave.settings import MEDIA_ROOT, MEDIA_URL, BASE_URL
from Profile.models import UserInfo


def user_directory_path(instance, filename):
    return os.path.join(MEDIA_ROOT, 'file/{0}/{1}/{2}'.format(instance.__class__.__name__,instance.post.id, filename))


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

    class Meta:
        abstract = True


class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)

    def url(self):
        return BASE_URL+MEDIA_URL+'file/{0}/{1}/{2}'.format(self.__class__.__name__,self.post.id, self.filename())

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        abstract = True


class Comment(models.Model):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(UserInfo, default='', on_delete=models.SET_DEFAULT)
    text = models.TextField()

    class Meta:
        abstract = True


class PostLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Team(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()


class TeamPost(Post):
    team = models.ForeignKey(Team, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    pass


class TeamFile(File):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class TeamComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class TeamLabel(PostLabel):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class PedigreePost(Post):
    pass


class PedigreeFile(File):
    post = models.ForeignKey(PedigreePost, on_delete=models.CASCADE)


class PedigreeComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(PedigreePost, on_delete=models.CASCADE)


class PedigreeLabel(PostLabel):
    post = models.ForeignKey(PedigreePost, on_delete=models.CASCADE)


class GreetingsPost(Post):
    pass


class GreetingsFile(File):
    post = models.ForeignKey(GreetingsPost, on_delete=models.CASCADE)


class GreetingsComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(GreetingsPost, on_delete=models.CASCADE)


class GreetingsLabel(PostLabel):
    post = models.ForeignKey(GreetingsPost, on_delete=models.CASCADE)


# 공지사항 게시판
class NoticePost(Post):
    pass


class NoticeFile(File):
    post = models.ForeignKey(NoticePost, on_delete=models.CASCADE)


class NoticeComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(NoticePost, on_delete=models.CASCADE)


class NoticeLabel(PostLabel):
    post = models.ForeignKey(NoticePost, on_delete=models.CASCADE)


class ShareInfoPost(Post):
    pass


class ShareInfoFile(File):
    post = models.ForeignKey(ShareInfoPost, on_delete=models.CASCADE)


class ShareInfoComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(ShareInfoPost, on_delete=models.CASCADE)


class ShareInfoLabel(PostLabel):
    post = models.ForeignKey(ShareInfoPost, on_delete=models.CASCADE)


class ANTAlgorithmPost(Post):
    pass


class ANTAlgorithmFile(File):
    post = models.ForeignKey(ANTAlgorithmPost, on_delete=models.CASCADE)


class ANTAlgorithmComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(ANTAlgorithmPost, on_delete=models.CASCADE)


class ANTAlgorithmLabel(PostLabel):
    post = models.ForeignKey(ANTAlgorithmPost, on_delete=models.CASCADE)


class CompetitionPost(Post):
    pass


class CompetitionFile(File):
    post = models.ForeignKey(CompetitionPost, on_delete=models.CASCADE)


class CompetitionComment(Comment):
    parent = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    post = models.ForeignKey(CompetitionPost, on_delete=models.CASCADE)


class CompetitionLabel(PostLabel):
    post = models.ForeignKey(CompetitionPost, on_delete=models.CASCADE)

