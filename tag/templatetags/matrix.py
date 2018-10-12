from django import template

register = template.Library()

@register.filter
def truncate(txt,nb):
	return txt[nb]

@register.filter
def exception(liste):
	return liste[1:]

@register.filter
def all_matieres(classe):
	all_mat = []
	for salle in classe.salles.all():
		for mat in salle.matieres.all():
			all_mat.append(mat)

	return list(set(all_mat))

@register.filter
def truncatepath(path,nb):
	tab = path.split('/')
	return tab[nb]

@register.filter
def nb_matiere(classes):
	nb = []
	for c in classes:
		for salle in c.salles.all():
			for m in salle.matieres.all():
				nb.append(m)
	return len(list(set(nb)))

@register.filter
def bold(obj,word):
	word = word.lower()
	new_word = ""
	for l in obj:
		if l.lower() in word:
			l = "<b class='text-primary'>"+l+"</b>"
		new_word += l
	return new_word

@register.filter
def showhour(obj):
	if '.30' in obj:
		obj = obj.replace(".30","")
		if int(obj) > 12:
			obj = int(obj) - 12
			obj = str(obj)+":30 PM"
		else:
			obj = str(obj)+":30 AM"
	else:
		if int(obj) > 12:
			obj = int(obj) - 12
			obj = str(obj)+":00 PM"
		else:
			obj = str(obj)+":00 AM"

	return obj

@register.filter
def hourstring(obj):
	if obj:
		h,m = str(obj).split(":")[0],str(obj).split(":")[1]
		return "%s:%s" % (h,m)
	return obj



	

