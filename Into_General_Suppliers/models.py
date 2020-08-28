from django.db import models
# from Into_General_Suppliers.models import Slider
from django.contrib.auth.models import User
# Create your models here.

class Service_Card(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	building = models.ImageField(default='default.jpg', upload_to='slide_images')
	building_content = models.TextField(default="name", max_length=1000)
	plumbing = models.ImageField(default='default.jpg', upload_to='slide_images')
	plumbing_content = models.TextField(default="name", max_length=1000)
	flooring = models.ImageField(default='default.jpg', upload_to='slide_images')
	flooring_content = models.TextField(default="name", max_length=1000)
	roofing = models.ImageField(default='default.jpg', upload_to='slide_images')
	roofing_content = models.TextField(default="name", max_length=1000)
	painting = models.ImageField(default='default.jpg', upload_to='slide_images')
	painting_content = models.TextField(default="name", max_length=1000)
	walling = models.ImageField(default='default.jpg', upload_to='slide_images')
	walling_content = models.TextField(default="name", max_length=1000)
	paving = models.ImageField(default='default.jpg', upload_to='slide_images')
	paving_content = models.TextField(default="name", max_length=1000)
	renovations = models.ImageField(default='default.jpg', upload_to='slide_images')
	renovations_content = models.TextField(default="name", max_length=1000)
	extentions = models.ImageField(default='default.jpg', upload_to='slide_images')
	extentions_content = models.TextField(default="name", max_length=1000)
	electricity = models.ImageField(default='default.jpg', upload_to='slide_images')
	electricity_content = models.TextField(default="name", max_length=1000)

	def __str__(self):
		return f'{self.user.username} Service_Card'

class message(models.Model):
	name = models.CharField(max_length=20)
	last_Name = models.CharField(max_length=20)
	email = models.EmailField(blank=True)
	message = models.TextField(blank=True, max_length=1000)
	subject = models.CharField(max_length=50)

	def __str__(self):
		return self.name + ' ' + self.last_Name
	
