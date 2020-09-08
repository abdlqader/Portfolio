from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=50,default='Job Title')
	summary = models.TextField()

	def __str__(self):
		return self.title