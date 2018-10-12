from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import django
from django.template.defaultfilters import slugify

import hashlib
import datetime
import random
import string

# Create your models here.


DECALAGE = 5

if settings.DEBUG:
	DECALAGE = 0


# WARNING: Don't edit this, unless you know what you do
def NOW():
	global DECALAGE
	return django.utils.timezone.now() - django.utils.timezone.timedelta(DECALAGE/24)


class UserProfile(models.Model):
	class Meta:
		permissions = (
				('is_user_only','Access as User Only'),

			)

	liste_sexe = [
		('M','Masculin'),
		('F','Féminin'),
		('A','Autres'),
	]

	liste_langues = [
		('HT','Creole'),
		('FR','French'),
		('EN',"English"),
	]

	date_created = models.DateTimeField(default=NOW)
	date_modified = models.DateTimeField(default=NOW)

	user = models.OneToOneField(User,unique=True,related_name='get_profile')
	slug = models.SlugField(blank=True)
	code = models.CharField(max_length=14)
	photo = models.ImageField(upload_to="profile_photo/%d-%m-%Y/", blank=True)
	phone = models.CharField(max_length=22,blank=True)
	national_id = models.CharField(max_length=18,blank=True)
	gender = models.CharField(max_length=50,blank=True,choices=liste_sexe,default='M')

	activation_key = models.CharField(max_length=255,blank=True)
	default_password = models.CharField(max_length=200,blank=True)
	date_key_expired = models.DateTimeField(blank=True,null=True)

	is_password_changed = models.BooleanField(default=True,blank=True)
	date_password_changed = models.DateTimeField(blank=True,null=True)
	is_account_confirmed = models.BooleanField(default=False)
	date_account_confirmed = models.DateTimeField(blank=True,null=True)

	cycle = models.CharField(max_length=255,blank=True)
	last_sex = models.DateTimeField(blank=True,null=True)

	language = models.CharField(default="EN",choices=liste_langues,max_length=2)
	
	nb_send_email = models.IntegerField(default=0)

	@property
	def first_name(self):
		return self.user.first_name

	@property
	def last_name(self):
		return self.user.last_name

	def generer(self,nb_letter):
		letters_digits = string.ascii_letters + string.digits
		aleatoire = [random.choice(letters_digits) for _ in range(nb_letter)]
		return ''.join(aleatoire)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.code = self.generer(14)
		self.slug = slugify(self.user.username)
		self.date_modified = NOW()
		super(UserProfile, self).save(*args, **kwargs)

	def __str__(self):
		return "%s %s [%s]" % (self.user.first_name,self.user.last_name,self.user.username)