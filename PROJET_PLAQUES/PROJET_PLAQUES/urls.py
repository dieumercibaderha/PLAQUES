"""
URL configuration for PROJET_PLAQUES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PLAQUES_APP.views import *
from django.conf import settings
from django.conf.urls.static import static
from ADMIN import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', connexion, name='connexion'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('testimonial/', testimonial, name='testimonial'), 
    path('idpro/', id_prop, name='idpro'),  
    path('idmoto/', Motoform, name='idmoto'),
    path('vente/', venteform, name='vente'),  
    path('controle/', controle, name='controle'),
    path('exo/', id_exo, name='exo'),  
    path('genre/', id_genre, name='genre'),
    path('pays/', id_pays, name='pays'),  
    path('utili/', id_utili, name='utili'),
    path('register/', register, name='registe'),  
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion' ),
    path('accounts/login/', connexion, name='connexion'),
    path('admin_ade/', include('ADMIN.urls', 'ADMIN')),
    path('modification_pro/', modifier_pro, name="modifier_pro"),
    path('supprimer_pro/', deletepro, name="supprimer_pro"),
    path('modvente/', modifier_vente, name='modvente'),
    path('supvente/', supvente, name='supvente'),
    path('modmoto/', modmoto, name="modmoto"),
    path('supmoto/', supmoto, name="supmoto"),
    path('modexo/', modexo, name="modexo"),
    path('supexo/', supexo, name="supexo"),
    path('logini/', logini, name="logini"),
    path('modgenre/', modgenre, name="modgenre"),
    path('supgenre/', supgenre, name="supgenre"),
    path('modutili/', modutili, name="modutili" ),
    path('suputili', suputili, name="suputili"),
    path('pdfgeneration/<str:pk>', pdf_generation, name="pdf_generation"),
    path('rose/<str:pk>', carte_rose, name="carterose"),
    path('listpropdf/', listpropdf, name="listpropdf"),
    path('listventepdf/', listventepdf, name="listventepdf"),
    path('listmotopdf/', listmotopdf, name="listmotopdf"),
    path('api/', include('API_PLAQUES.urls'))
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)