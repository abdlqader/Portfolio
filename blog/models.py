from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=True)
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def pub_date_fancy(self):
		return self.pub_date.strftime(' %d of %B, %Y')

	def summery(self):
		result = self.body.split(' ')[:10]
		return ' '.join(result)