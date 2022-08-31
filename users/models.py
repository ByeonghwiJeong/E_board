from django.db import models

class User(models.Model):
    name          = models.CharField(max_length = 45)
    email         = models.CharField(max_length = 45)
    password      = models.CharField(max_length = 200)
    phone         = models.CharField(max_length = 40)
    gender        = models.IntegerField() # M : 1, F :  2
    age           = models.IntegerField()
    authorization = models.IntegerField(default=1)
    created_at    = models.DateTimeField(auto_now_add=True)
    connected_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'


class UserLog(models.Model):
    user     = models.ForeignKey('users.User', on_delete=models.CASCADE)
    gender   = models.IntegerField()
    age      = models.IntegerField()
    log_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'logs'
