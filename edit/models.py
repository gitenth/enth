from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	title =  models.CharField(max_lengt = 50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_at = DateTimeField(auto_now_add = True)
	question = ForeignKey(Question)
	author = ForeignKey(User)
