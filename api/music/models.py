from django.db import models

# Create your models here.
class Songs(models.Model):
	title = models.TextField()
	artist = models.TextField()
	new = models.TextField(null = True)

class Test(models.Model):
	f1 = models.BooleanField()
	f2 = models.TextField()


