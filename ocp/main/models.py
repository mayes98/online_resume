import uuid
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from django.db.models import Q
from bs4 import BeautifulSoup

CustomUser = get_user_model()

class Skill(models.Model):
	class Meta:
		verbose_name_plural = 'skills'
		verbose_name = 'skill'

	name = models.CharField(max_length=20, blank=True, null=True)
	score = models.IntegerField(default=80, blank=True, null=True)
	image = models.FileField(blank=True, null=True, upload_to="skills")
	is_key_skill = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class UserProfile(models.Model):

	class Meta:
		verbose_name = 'User Profile'
		verbose_name_plural = 'User Profiles'

	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
	title = models.CharField(max_length=200, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	skills = models.ManyToManyField(Skill, blank=True)
	cv = models.FileField(blank=True, null=True, upload_to="cv")

	def __str__(self):
		return f'{self.user.username}'

class ContactProfile(models.Model):

	class Meta:
		verbose_name_plural = 'Contact Profiles'
		verbose_name = 'Contact Profile'
		ordering = ["timestamp"]

	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(verbose_name="Name", max_length=100)
	email = models.EmailField(verbose_name="Email")
	message = models.TextField(verbose_name="message")

	def __str__(self):
		return f'{self.name}'

class Testimonial(models.Model):

	class Meta:
		verbose_name_plural = 'Testimonials'
		verbose_name = 'Testimonial'
		ordering = ["name"]

	thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonial")
	name = models.CharField(max_length=200, blank=True, null=True)
	role = models.CharField(max_length=200, blank=True, null=True)
	quote = models.CharField(max_length=500, blank=True, null=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

		
class Portfolio(models.Model):

	class Meta:
		verbose_name_plural = 'Portfolios'
		verbose_name = 'Portfolio'
		ordering = ["name"]

	id = models.UUIDField(
		primary_key = True,
		default = uuid.uuid4,
		editable = False)
	date = models.DateTimeField(blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	body = RichTextField(blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to="main/portfolios")
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main:portfolio_detail', args=[str(self.id)])

	def html_to_text(self, *args, **kwargs):
		soup = BeautifulSoup(self.body, features="html.parser")
		text = soup.get_text()
		return text


class BlogQuerySet(models.QuerySet):
	def search(self, query=None):
		if query is None or query == "":
			return self.none()
			print("No matching information found")
		lookups = Q(title__icontains=query) | Q(body__icontains=query)
		return self.filter(lookups)

class BlogManager(models.Manager):
	def get_queryset(self):
		return BlogQuerySet(self.model, using=self._db)

	def search(self, query=None):
		return self.get_queryset().search(query=query)

class Blog(models.Model):

	class Meta:
		verbose_name_plural = 'Blogs'
		verbose_name = 'Blog'
		ordering = ["-timestamp"]

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=200, blank=True, null=True)
	title = models.CharField(max_length=200, blank=True, null=True)
	body = RichTextField(blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to="main/blogs")
	is_active = models.BooleanField(default=True)

	objects=BlogManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('main:blog_detail', args=[str(self.id)])

	def html_to_text(self, *args, **kwargs):
		soup = BeautifulSoup(self.body, features="html.parser")
		text = soup.get_text()
		return text

class Certificate(models.Model):

	class Meta:
		verbose_name_plural = 'Certificates'
		verbose_name = 'Certificate'

	date = models.DateTimeField(blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	title = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=500, blank=True, null=True)
	is_active = models.BooleanField(default= True)

	def __str__(self):
		return self.name
