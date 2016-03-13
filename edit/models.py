from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	class Meta:
		db_table = 'question'
	title =  models.CharField(max_length=50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')

class Answer(models.Model):
	class Meta:
		db_table = 'answer'
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)