from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^hopitaux-proches$', views.hopitauxProches,name="hopitauxProches"),
    url(r'^children$', views.children,name="children"),
    url(r'^contraception$', views.contraception,name="contraception"),
    url(r'^pregnant$', views.pregnant,name="pregnant"),
    url(r'^doctors$', views.doctors,name="doctors"),
    url(r'^appointment$', views.appointment,name="appointment"),
    url(r'^contact$', views.contact,name="contact"),
    url(r'^contraception-details$', views.contraceptionDetails,name="contraceptionDetails"),
    url(r'^change-language/$',views.changeLanguage,name='changeLanguage'),
    url(r'^getDataForMap/$',views.getDataForMap,name='getDataForMap'),
    url(r'^login/$',views.loginView,name='loginView'),
    url(r'^signup/$',views.signupView,name='signupView'),
    url(r'^logout/$',views.logoutView,name='logout'),
]
