from django.db import models


class Notice(models.Model):
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        db_table = 'notice'


class FreeBoard(models.Model):
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        db_table = 'freeboard'


class AdminBoard(models.Model):
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        db_table = 'adminboard'