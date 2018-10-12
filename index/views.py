from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Permission
from django.contrib import messages
from django.core.urlresolvers import resolve, Resolver404
from django.http import JsonResponse, HttpResponseRedirect

from .models import UserProfile
import hashlib
import datetime
import random

# Create your views here.


def index(request):
	context = {}
	return render(request,"index/index.html",context)

def changeLanguage(request):
	url = request.GET.get("next")
	lg = request.GET.get("lg")

	if url:
		try:
			resolve(url)
			response = redirect(url)
		except Resolver404:
			response = redirect(home)

	if lg == "EN" or lg == "FR" or lg == "HT":
		if request.user.is_authenticated():
			up = request.user.get_profile
			up.language = lg
			up.save()
		else:
			response.set_cookie('lg_ch',lg)  # GET IT FROM COOKIES

	return response


def hopitauxProches(request):
	context = {}
	return render(request,"index/hopitaux-proches.html",context)

def children(request):
	if request.method == 'POST':
		m = int(request.POST.get("m"))
		d = int(request.POST.get("d"))
		y = int(request.POST.get("y"))

		date = datetime.date(y,m,d)

		up = request.user.get_profile
		up.last_sex = date
		up.save()


	context = {
		'today':datetime.datetime.today(),
		'range_jour':range(1,32),
	}
	return render(request,"index/children.html",context)

def contraception(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/contraception-details?rd="+request.user.get_profile.gender)
	context = {
		'today':datetime.datetime.today(),
		'range_jour':range(1,32),
	}
	return render(request,"index/contraception.html",context)

def contraceptionDetails(request):
	context = {
		'today':datetime.datetime.today(),
		'range_jour':range(1,32),
	}
	return render(request,"index/contraception-details.html",context)

def getDataForMap(request):
	''' On envoie les donnees pour afficher dans la carte '''
	data = {}
	if request.is_ajax():
		if request.method == 'GET':
			for d in Demande.objects.all():
				data["data-"+str(d.id)] = {
					'categorie':d.categorie.nom.lower(),
					'ville':d.localite.commune.nom.upper(),
					'id':d.id,
					'lat':d.lati,
					'lng':d.longi,
					'description':d.description,
				}
	return JsonResponse(data)

def logoutView(request):
	try:
		logout(request)
		if request.GET['next']:
			return redirect(request.GET['next'])
		return redirect("index")
	except:
		return redirect("index")

def loginView(request):
	data = {}
	data['erreur'] = True
	if request.user.is_authenticated():#Gere l'introduction des urls.
		return redirect(index)

	url = request.GET.get('url')
	if request.method == 'POST':
		
		username = request.POST.get('username')
		if username:
			username = username.strip().lower()
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user: # Si l'USER est authentifié, on le connecte
			logout(request)
			login(request,user)
			data['erreur'] = False

	return JsonResponse(data)

# def signupView(request):
# 	data = {}
# 	data['erreur'] = True
# 	if request.user.is_authenticated():#Gere l'introduction des urls.
# 		return redirect(index)

# 	url = request.GET.get('url')
# 	if request.method == 'POST':
		
# 		fullname = request.POST.get('username')
# 		if username:
# 			username = username.strip().lower()
# 		password = request.POST.get('password')
# 		user = authenticate(username=username, password=password)

# 		if user: # Si l'USER est authentifié, on le connecte
# 			logout(request)
# 			login(request,user)
# 			data['erreur'] = False

# 	return JsonResponse(data)



def signupView(request):
	if request.user.is_authenticated():
		return redirect(index)

	data = {'erreur':True}
	if request.method == 'POST':
		first_name= request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		birthday = request.POST.get("birthday")
		sex = request.POST.get("sex")
		password =request.POST.get("password")
		cycle = request.POST.get("cycle")

		salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
		activation_key = hashlib.sha1((salt+first_name).encode()).hexdigest()
		date_key_expired = datetime.datetime.today() + datetime.timedelta(2)

		username = first_name
		user = User.objects.create(username=username,first_name=first_name,last_name=last_name)

		user.set_password(password)
		user.save()

		up = UserProfile(
			user=user,
			date_key_expired = date_key_expired,
			activation_key = activation_key,
			default_password = password,
			gender = sex
			)
		up.save()

		
		logout(request)
		signin_user = authenticate(username=user.username, password=password)

		login(request,signin_user)
		data['erreur'] = False

	return JsonResponse(data)


def pregnant(request):
	context = {}
	return render(request,"index/pregnant.html",context)

def doctors(request):
	context = {}
	return render(request,"index/doctors.html",context)

def appointment(request):
	context = {}
	return render(request,"index/appointement.html",context)

def contact(request):
	context = {}
	return render(request,"index/contact.html",context)