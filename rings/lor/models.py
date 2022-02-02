from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager


# Create your models here.

class Favorite(models.Model):
	objects = InheritanceManager()
	user_id = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
	character_id = models.CharField(max_length=60, unique=True, default="")
	
	def __str__(self):
		return self.character_id


class Quote(Favorite):
	quote_id = models.CharField(max_length=60, unique=True)
	
	def __str__(self):
		return self.quote_id
