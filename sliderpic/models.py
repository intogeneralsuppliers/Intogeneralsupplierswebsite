from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Home_Page(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} Home_Page'

class Logo(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	images = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} Logo_Page'

class Services_Page(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	service = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} Services_Page'

class About_Page(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	about_pic = models.ImageField(default='default.jpg', upload_to='slide_images')
	about_pic2 = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} About_Page'

class Contact_Page(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	contact_pic = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} Contact_Page'

class Projects_Page(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	project = models.ImageField(default='default.jpg', upload_to='slide_images')
	project2 = models.ImageField(default='default.jpg', upload_to='slide_images')


	def __str__(self):
		return f'{self.user.username} Projects'

class Building(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	building1 = models.ImageField(default='default.jpg', upload_to='building_images')
	building2 = models.ImageField(default='default.jpg', upload_to='building_images')
	building3 = models.ImageField(default='default.jpg', upload_to='building_images')
	building4 = models.ImageField(default='default.jpg', upload_to='building_images')
	building5 = models.ImageField(default='default.jpg', upload_to='building_images')


	def __str__(self):
		return f'{self.user.username} Plumbing'

class Plumbing(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	plumbing1 = models.ImageField(default='default.jpg', upload_to='plumbing_images')
	plumbing2 = models.ImageField(default='default.jpg', upload_to='plumbing_images')
	plumbing3 = models.ImageField(default='default.jpg', upload_to='plumbing_images')
	plumbing4 = models.ImageField(default='default.jpg', upload_to='plumbing_images')
	plumbing5 = models.ImageField(default='default.jpg', upload_to='plumbing_images')


	def __str__(self):
		return f'{self.user.username} Plumbing'

class Flooring(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	flooring1 = models.ImageField(default='default.jpg', upload_to='flooring_images')
	flooring2 = models.ImageField(default='default.jpg', upload_to='flooring_images')
	flooring3 = models.ImageField(default='default.jpg', upload_to='flooring_images')
	flooring4 = models.ImageField(default='default.jpg', upload_to='flooring_images')
	flooring5 = models.ImageField(default='default.jpg', upload_to='flooring_images')

	def __str__(self):
		return f'{self.user.username} Flooring'

class Roofing(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	roofing1 = models.ImageField(default='default.jpg', upload_to='roofing_images')
	roofing2 = models.ImageField(default='default.jpg', upload_to='roofing_images')
	roofing3 = models.ImageField(default='default.jpg', upload_to='roofing_images')
	roofing4 = models.ImageField(default='default.jpg', upload_to='roofing_images')
	roofing5 = models.ImageField(default='default.jpg', upload_to='roofing_images')

	def __str__(self):
		return f'{self.user.username} Roofing'

class Painting(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	painting1 = models.ImageField(default='default.jpg', upload_to='painting_images')
	painting2 = models.ImageField(default='default.jpg', upload_to='painting_images')
	painting3 = models.ImageField(default='default.jpg', upload_to='painting_images')
	painting4 = models.ImageField(default='default.jpg', upload_to='painting_images')
	painting5 = models.ImageField(default='default.jpg', upload_to='painting_images')

	def __str__(self):
		return f'{self.user.username} Painting'

class Walling(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	walling1 = models.ImageField(default='default.jpg', upload_to='walling_images')
	walling2 = models.ImageField(default='default.jpg', upload_to='walling_images')
	walling3 = models.ImageField(default='default.jpg', upload_to='walling_images')
	walling4 = models.ImageField(default='default.jpg', upload_to='walling_images')
	walling5 = models.ImageField(default='default.jpg', upload_to='walling_images')

	def __str__(self):
		return f'{self.user.username} Walling'

class Paving(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	paving1 = models.ImageField(default='default.jpg', upload_to='paving_images')
	paving2 = models.ImageField(default='default.jpg', upload_to='paving_images')
	paving3 = models.ImageField(default='default.jpg', upload_to='paving_images')
	paving4 = models.ImageField(default='default.jpg', upload_to='paving_images')
	paving5 = models.ImageField(default='default.jpg', upload_to='paving_images')

	def __str__(self):
		return f'{self.user.username} Paving'

class Renovation(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	renovation1 = models.ImageField(default='default.jpg', upload_to='renovation_images')
	renovation2 = models.ImageField(default='default.jpg', upload_to='renovation_images')
	renovation3 = models.ImageField(default='default.jpg', upload_to='renovation_images')
	renovation4 = models.ImageField(default='default.jpg', upload_to='renovation_images')
	renovation5 = models.ImageField(default='default.jpg', upload_to='renovation_images')

	def __str__(self):
		return f'{self.user.username} Renovation'

class Extention(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	extention1 = models.ImageField(default='default.jpg', upload_to='extention_images')
	extention2 = models.ImageField(default='default.jpg', upload_to='extention_images')
	extention3 = models.ImageField(default='default.jpg', upload_to='extention_images')
	extention4 = models.ImageField(default='default.jpg', upload_to='extention_images')
	extention5 = models.ImageField(default='default.jpg', upload_to='extention_images')

	def __str__(self):
		return f'{self.user.username} Extention'

class Electricity(models.Model):
	user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
	electricity1 = models.ImageField(default='default.jpg', upload_to='electricity_images')
	electricity2 = models.ImageField(default='default.jpg', upload_to='electricity_images')
	electricity3 = models.ImageField(default='default.jpg', upload_to='electricity_images')
	electricity4 = models.ImageField(default='default.jpg', upload_to='electricity_images')
	electricity5 = models.ImageField(default='default.jpg', upload_to='electricity_images')

	def __str__(self):
		return f'{self.user.username} Electricity'

