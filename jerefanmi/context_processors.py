from index.models import *
import hashlib
import datetime
import random

# Create yout global context here


def Global(request):
	if request.user.is_authenticated():
		user = request.user
		lg_ch = ''
		try:
			lg_ch = user.get_profile.language
		except:
			activation_key = hashlib.sha1((str(random.random())).encode()).hexdigest()
			date_key_expired = datetime.datetime.today() + datetime.timedelta(2)
			up = UserProfile(
				user=user,
				date_key_expired = date_key_expired,
				activation_key = activation_key,
				is_account_confirmed = True,
				)
			up.save()
	else:
		lg_ch = request.COOKIES.get('lg_ch')
		if lg_ch != "EN" and lg_ch != "FR" and lg_ch != "HT":
			lg_ch = "HT"
	
	icon_bar = request.session.get('icon_bar')
	if icon_bar is None:
		icon_bar = 'visible'

	return {
		'lg_ch':lg_ch,
		'session_email':request.session.get('email_or_phone'),
		'icon_bar':icon_bar,
	}
