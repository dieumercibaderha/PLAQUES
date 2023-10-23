import datetime
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse, HttpResponse
from .models import *
from .formoto import *
from .forvente import Venteform
import qrcode

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.views.decorators import gzip
from django.conf import settings
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.core.paginator  import (Paginator, EmptyPage, PageNotAnInteger)
# Create your views here.



@login_required
def carte_rose(request, pk):
     ids=Enregistrement.objects.get(id=pk)
     plaque=ids.Num_Plaque
     
     img=qrcode.make(plaque)
     img.save('D:\PROJETS_TFC\PROJET_PLAQUES\PLAQUES_APP\static\images/qrid.png')
     
     exo=ids.Exonerations
     idmoto=ids.moto
     motoinstance=Moto.objects.get(Nom=idmoto)
     motomarque=motoinstance.Marque
     mototype=motoinstance.Type_utilisation
     motonom=motoinstance.Nom
     motoanne=motoinstance.Annee
     motosource=motoinstance.Source_energie
     motocouleur=motoinstance.Couleur
     motopays=motoinstance.Pays_fabrication
     motodate=motoinstance.Date_circulation
     motogenre=motoinstance.genre_moto
     motochassis=motoinstance.Num_chassis
     motomoteur=motoinstance.Num_moteur
     motopro=motoinstance.proprietaire 
     proinstance=Proprietaires.objects.get(nom=motopro)
     proadresse=proinstance.adresse
     pronom=proinstance.nom
     protel=proinstance.Tel
     genres=Genre.objects.all()
     uti=Utilisation.objects.all()
     
     context={
          'plaque':plaque,
          'motomarque':motomarque,
          'mototype':mototype,
          'motonom':motonom,
          'motoanne':motoanne,
          'motosource':motosource,
          'motocouleur':motocouleur,
          'motopays':motopays,
          'motodate':motodate,
          'motogenre':motogenre,
          'motochassis':motochassis,
          'motomoteur':motomoteur,
          'motopro':motopro,
          'proadresse':proadresse,
          'protel':protel,
          'genres':genres,
          'exo':exo,
          'pronom':pronom       
     }  
     font_config=FontConfiguration()
     html_templates=get_template("rose.html").render(context)
     pdf_file=HTML(string=html_templates).write_pdf(stylesheets=[CSS(string='''
                                                                      @page{
                                                                           size:A4;
                                                                           margin-left: 2cm;
                                                                           margin-top: 2px;}
                                                                         .qr{
                                                                              margin-left:6;
                                                                         }
                                                                         ''')])
     response=HttpResponse(pdf_file, content_type='application/pdf')
     response['Content-Disposition']='filename="carte_rose.pdf"'
     return response


@login_required
def listpropdf(request):
     listprop=Proprietaires.objects.all()
     context={
          'listprop':listprop
     }
     templates=get_template("listpropdf.html").render(context)
     pdf_file=HTML(string=templates).write_pdf(stylesheets=[CSS(string='''
                                                                      @page{
                                                                           size:A4;
                                                                           margin-left:1cm;
                                                                           margin-top:1cm;}
                                                                         .qr{
                                                                              margin-left:6;
                                                                         }
                                                                         '''
                                                                           )])
     response=HttpResponse(pdf_file, content_type='application/pdf')
     response['Content-Disposition']='filename="liste_membre.pdf"'
     return response

@login_required
def listventepdf(request):
     listvente=Enregistrement.objects.all()
     context={
          'listvente':listvente
     }
     templates=get_template("listventedf.html").render(context)
     pdf_file=HTML(string=templates).write_pdf(stylesheets=[CSS(string='''
                                                                      @page{
                                                                           size:A4;
                                                                           margin-left:0.5cm;
                                                                           margin-top:1cm;
                                                                           display:paysage;}
                                                                        
                                                                         ''')])
     response=HttpResponse(pdf_file, content_type='application/pdf')
     response['Content-Disposition']='filename="liste_vente.pdf"'
     return response
@login_required
def listmotopdf(request):
     listmoto=Moto.objects.all()
     context={
          'listmoto':listmoto
     }
     templates=get_template("listmotopdf.html").render(context)
     pdf_file=HTML(string=templates).write_pdf(stylesheets=[CSS(string='''
                                                                      @page{
                                                                           size:A4;
                                                                           margin-left:0.5cm;
                                                                           margin-top:1cm;
                                                                           display:paysage;}
                                                                        
                                                                         ''')])
     response=HttpResponse(pdf_file, content_type='application/pdf')
     response['Content-Disposition']='filename="liste_moto.pdf"'
     return response


@login_required
def pdf_generation(request, pk):
     try:  
          ventef=Enregistrement.objects.get(Proprietaire=pk)
          qrmoto=ventef.moto
          nump=ventef.Num_Plaque
          proqr=ventef.Proprietaire
          phoqr=ventef.Photo_proprietaire
          exoqr=ventef.Exonerations
          datesqr=ventef.dates    
          contextqr={
                         'qrmoto':qrmoto,
                         'nump':nump,
                         'proqr':proqr,
                         'phoqr':phoqr,
                         'exoqr':exoqr,
                         'datesqr':datesqr       
                    }
          img=qrcode.make(nump)
          img.save('D:\PROJETS_TFC\PROJET_PLAQUES\PLAQUES_APP\static\images/qrprop.png')
          dategen=datetime.datetime.today()
          objpro=Proprietaires.objects.get(id=pk)
          noms=objpro.nom 
          ad=objpro.adresse
          mai=objpro.Mail
          te=objpro.Tel
          pho=objpro.Photo
          context={
                    'id':pk,
                    'nom':noms,
                    'addresse':ad,
                    'mail':mai,
                    'tele':te,
                    'photo':pho       
                    }   
          font_config=FontConfiguration()
          html_templates=get_template("cartepdf.html").render(context)
          pdf_file=HTML(string=html_templates).write_pdf(stylesheets=[CSS(string='''
                                                                      @page{
                                                                           size:A4(35mm, 45mm);
                                                                           margin-left: 6cm;
                                                                           margin-top:6cm;
                                                                           
                                                                      }
                                                                      .titrepied{
                                                                           margin-top:0%;
                                                                           font-size: 3px;
                                                                           margin
                                                                      }
                                                                      
                                                                      .titre_cota h1{font-style:normal;font-weight: bold;font-size: 20px;color: rgb(74, 74, 138);font-family: fantasy;margin-top: -1%;text-shadow: 0.1ch 2px rgb(156, 154, 154);} 
                                                                      .pieds{height: 20%;margin-top:-3% ;
                                                                      background-color: rgb(209, 203, 203)}
                                                                      .pieds p{font-size: 6px; margin-top:-1.7% } 
                                                                      .carte{background-color:aliceblue;
                                                                      border-radius: 20%;} 
                                                                      .entete{background-color: rgb(209, 203, 203);
                                                                      width: 100%;height: 22%; border-top-left-radius: 3%;
                                                                      border-top-right-radius: 3%;
                                                                      align-items:stretch;}
                                                                      .entete img{padding-top: 32%;  width: 40px; height: 30px;}
                                                                      .logo{ margin-left:4%;margin-top:-2%;}
                                                                      .drapeau{margin-right:10%; margin-top:-2%; margin-left: -2%}
                                                                      .titre_cota h1{font-style:normal;
                                                                      font-weight: bold;font-size: 15px;color: rgb(74, 74, 138);
                                                                      font-family: fantasy;margin-top: -1%;
                                                                      text-shadow: 0.1ch 2px rgb(156, 154, 154);}
                                                                      .body-body{ margin-left: 20%;}.body-body 
                                                                      .identite{font-size: 7px;text-align: left;
                                                                      margin-top: -8%;
                                                                      font-family: Tahoma, Geneva, Verdana;}
                                                                      .corps img{ margin-left: 20%; margin-top: 25%;
                                                                      border-radius: 20%;}.corps 
                                                                      .i{ margin-left: 2%;margin-top: -5%;}
                                                                      .titre_cota h4{margin-left: 3%;
                                                                      font-size: 10px;background-color: rgb(167, 34, 34)
                                                                      ;color: white;
                                                                      font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;border-radius: 25%;margin-top: -10%;}
                                                                      
                                                                      .titre h3{font-family:cursive;font-weight: bolder; 
                                                                      font-size: 7px;  }.titre h2{font-size: 10px;margin-left: 1%;  text-align: center;}
                                                                      
                                                                      .pieds{ height: 20%; 
                                                                      margin-top:-1% ;background-color: rgb(209, 203, 203);}
                                                                      .pieds p{font-size: 6px;
                                                                      margin-top:1%;}''', 
                                                                      font_config=font_config)])
          response=HttpResponse(pdf_file, content_type='application/pdf')
          response['Content-Disposition']='filename="home_page.pdf"'
          return response
     except:
          ventef=Proprietaires.objects.get(id=pk)
          proqr=ventef.nom
          return render(request,"erreurcarte1.html", {'pro':proqr})

@login_required
def index(request):
     return render(request, "index.html")

@login_required
def about(request):
     return render(request, "about.html")

@login_required
def contact(request):
     return render(request, "contact.html")

@login_required
def news(request):
     return render(request, "news.html")

@login_required
def testimonial(request):
     return render(request, "testimonial.html")


@login_required
def service(request):
     return render(request, "service.html")
@login_required
def id_prop(request):
     
     forpro=Proforms(request.POST or None, request.FILES)
     messages=""
     listprop=Proprietaires.objects.all()
     if forpro.is_valid():
          forpro.save()
          forpro=Proforms()
          messages="Enregistrement reussi "
     
     listprop=Proprietaires.objects.all()
     if request.GET:
          rech=request.GET.get('recherche')
          if rech is not None:
               listprop=Proprietaires.objects.filter(nom__icontains=rech)
              
        
     context={
               'listprop':listprop,
               'ms':messages,
               'forpro':forpro,
          }
     default_page=1
     page=request.GET.get('page', default_page)
     items_par_page=3
     paginator=Paginator(listprop, items_par_page)
     try:
          items_page=paginator.page(page) 
     except PageNotAnInteger:
          items_page=paginator.page(default_page)

     except EmptyPage:
          items_page=paginator.page(paginator.num_pages)  
     context['listprop']=items_page
     
     return render(request, "modpro.html", context)
@login_required
def modifier_pro(request):
     if request.method=="POST":
          pk=request.POST.get("id")
          Nom=request.POST.get("nom")
          Addresse=request.POST.get("addresse")
          mail=request.POST.get("mail")
          tele=request.POST.get("tel")
          ph=Proprietaires.objects.get(id=pk)
          if request.POST:
               g=Proprietaires.objects.filter(id=pk).update(nom=Nom, adresse=Addresse, Mail=mail, Tel=tele, Photo=ph.Photo)
               

               return redirect("idpro")
          
     return redirect("idpro")

@login_required    
def deletepro(request):
    pk=request.POST.get("id")
    obj=Proprietaires.objects.get(id=pk)
    if request.POST:
        obj.delete()
        return redirect("idpro")
     
    return redirect("idpro")    
     
@login_required
def Motoform(request):
     formmoto=Motoforms(request.POST or None)
     messages=""
     listmoto=Moto.objects.all()
     if formmoto.is_valid():
          formmoto.save()
          formmoto=Motoforms()
          messages="Enregistrement reussi "
     
     context={'form':formmoto, 
              'mes':messages, 
              'listmoto':listmoto, 
              'listprop':Proprietaires.objects.all(), 
                                             
               'listutili':Utilisation.objects.all(), 
               'listpays':Pays.objects.all(), 
               'listgenre':Genre.objects.all()}
     
     default_page=1
     page=request.GET.get('page', default_page)
     items_par_page=3
     paginator=Paginator(listmoto, items_par_page)
     try:
          items_page=paginator.page(page) 
     except PageNotAnInteger:
          items_page=paginator.page(default_page)

     except EmptyPage:
          items_page=paginator.page(paginator.num_pages)  
     context['listmoto']=items_page
     
     return render(request, "id_moto.html", context )

@login_required
def modmoto(request):
     pk=request.POST.get("id")
     datec=Moto.objects.get(id=pk)
     marque=request.POST.get("marque")
     nom=request.POST.get("nom")
     genre=request.POST.get("genre")
     couleur=request.POST.get("couleur")
     source=request.POST.get("source")
     utilisation=request.POST.get("utilisation")
     pays=request.POST.get("pays")
     nchassis=request.POST.get("nchassis")
     nmoteur=request.POST.get("nmoteur")
     pro=request.POST.get("proprietaire")
     datec=Moto.objects.get(id=pk)
     utilisation=request.POST.get("utilisation")
     
     if request.POST:
          g=Moto.objects.filter(id=pk).update(Marque=marque,Nom=nom,genre_moto=genre,
                                              Couleur=couleur, Source_energie=source, 
                                              Type_utilisation=utilisation,
                                              Pays_fabrication=pays,
                                              Num_chassis=nchassis, Num_moteur=nmoteur,
                                              Date_circulation=datec.Date_circulation, 
                                              Date_identification=datec.Date_identification, proprietaire=pro)
          return redirect('idmoto')
     return redirect('idmoto')


@login_required
def supmoto(request):
     pk=request.POST.get("id")
     obj=Moto.objects.get(id=pk)
     if request.POST:
          obj.delete()
          return redirect('idmoto')
     return redirect('idmoto')

@login_required
def venteform(request):
     formvente=Venteform(request.POST or None, request.FILES)
     listvente=Enregistrement.objects.all()
     
     try:
          if request.method=="POST":
               moto=request.POST.get("moto")
               motos=Moto.objects.get(id=moto)
               idmoto=Moto.objects.get(id=moto)
               plaque=request.POST.get("num_plaque")
               pro=idmoto.proprietaire
               idph=Proprietaires.objects.get(nom=pro)
               photopro=idph.Photo
               exo=request.POST.get("exoneration")
               exos=Exoneration.objects.get(id=exo)
               if request.POST:
                    g=Enregistrement.objects.create(moto=motos, Num_Plaque=plaque, Proprietaire=pro, Photo_proprietaire=photopro, Exonerations=exos)
                    

                    return redirect("vente")
     
    
          if request.GET:
               rech=request.GET.get('recherche')
               if rech is not None:
                    listvente=Enregistrement.objects.filter(Num_Plaque=rech)
                    if listvente:
                    
                         nump=rech
                         f=Enregistrement.objects.get(Num_Plaque=rech)
                         e=f.Exonerations
                         p=f.Proprietaire
                         c=Controle.objects.create(Num_Plaque=nump,
                                                       Exonerations=e,
                                                       Proprietaires=p
                                                       )

                         c.save()
                         
          context={'listvente':listvente,
                    'formvente':formvente,'listprop':Proprietaires.objects.all(),
                    'listexon':Exoneration.objects.all(), 'listmoto':Moto.objects.all()
                    }
          default_page=1
          page=request.GET.get('page', default_page)
          items_par_page=3
          paginator=Paginator(listvente, items_par_page)
          try:
               items_page=paginator.page(page) 
          except PageNotAnInteger:
               items_page=paginator.page(default_page)

          except EmptyPage:
               items_page=paginator.page(paginator.num_pages)  
          context['listvente']=items_page
               
          return render(request, 'vente.html', context)
          
     except:
          if request.method=="POST":
               moto=request.POST.get("moto")
               motos=Moto.objects.get(id=moto)
               mono=motos.Nom
          return render(request, "erreurcarte.html", {'mono':mono})
     
     
    

@login_required
def modifier_vente(request):
     pk=request.POST.get("id")
     moto=request.POST.get("moto")
     motos=Moto.objects.get(id=moto)
     idmoto=Moto.objects.get(id=moto)
     plaque=request.POST.get("num_plaque")
     pro=idmoto.proprietaire
     idph=Proprietaires.objects.get(nom=pro)
     photopro=idph.Photo
     exo=request.POST.get("exoneration")
     exos=Exoneration.objects.get(id=exo)
     if request.POST:
          u=Enregistrement.objects.filter(id=pk).update(moto=motos, Num_Plaque=plaque, Proprietaire=pro, 
                                                        Photo_proprietaire=photopro, Exonerations=exos)
          return redirect('vente')
     
     return redirect('vente')
@login_required
def supvente(request):
     pk=request.POST.get("id")
     obj=Enregistrement.objects.get(id=pk)
     if request.POST:
          obj.delete()
          return redirect('vente')
     return redirect('vente')
     
@login_required   
def controle(request):
     listvente=Controle.objects.all()
     listfilte=Controle.objects.all()
     erreur="invalide plaque"
     contro=""
     if request.GET:
          rech=request.GET.get('recherche')
          if rech is not None:
               listfilte=Controle.objects.filter(Num_Plaque=rech)
               for l in listfilte:
                    
                    if l.Exonerations != "NON-EXONERATION":
                         contro="cette moto est exoneré par tout autre forme de controle excepté le controle des plaques"
                         
                         return render(request, "controle.html", {'listvente':listvente, 'listfilte':listfilte,'erreur':erreur, 'contro':contro })
               erreur="invalide plaque"

          else:
               erreur="Plaque invalide"
     
    
     
     return render(request, "controle.html", {'listvente':listvente, 'listfilte':listfilte,'erreur':erreur, 'contro':contro })

@login_required
def id_pays(request):
     form=Paysforms(request.POST or None, request.FILES )
     if form.is_valid():
          form.save()
          form=Paysforms()
     listpays=Pays.objects.all()
     context={
          'listpays':listpays
     }
     
     return render(request, "id_pays.html", context)

@login_required
def id_utili(request):
     form=Utiliforms(request.POST or None, request.FILES )
     if form.is_valid():
          form.save()
          form=Utiliforms()
     return render(request, 'id_utili.html', {'form':form, 'listutili':Utilisation.objects.all()})

@login_required
def modutili(request):
     pk=request.POST.get("id")
     utilis=request.POST.get("utili")
     des=request.POST.get("description") 
     if request.POST:
          u=Utilisation.objects.filter(id=pk).update(Type_utilisation=utilis, Description=des)
          return redirect('utili')
     
     return redirect('utili')

@login_required
def suputili(request):
     pk=request.POST.get("id")
     obj=Utilisation.objects.get(id=pk)
     if request.POST:
          obj.delete()
     
     return redirect('utili')




   



@login_required
def id_genre(request):
     formgenre=Genreforms(request.POST or None)
     listgenre=Genre.objects.all()
     
     if formgenre.is_valid():
          formgenre.save()
          formgenre=Genreforms()
     context={
          'listgenre':listgenre,
          'formgenre':formgenre
     }
     
     return render(request, "id_genre.html", context)
@login_required
def modgenre(request):
     pk=request.POST.get("id")
     ge=request.POST.get("genre")
     des=request.POST.get("description") 
     if request.POST:
          u=Genre.objects.filter(id=pk).update(Genre=ge, Description=des)
          return redirect('genre')
     
     return redirect('genre')
@login_required
def supgenre(request):
     pk=request.POST.get("id")
     obj=Genre.objects.get(id=pk)
     if request.POST:
          obj.delete()
     
     return redirect('genre')

@login_required
def id_exo(request):
     form=Exoforms(request.POST or None)
     listexo=Exoneration.objects.all()
     if form.is_valid():
          form.save()
          form=Exoforms()
     context={
          'listexo':listexo,
          'formexo':form
     }
     return render(request, "id_exo.html", context)

@login_required
def modexo(request):
     pk=request.POST.get("id")
     type=request.POST.get("type")
     des=request.POST.get("des") 
     if request.POST:
          u=Exoneration.objects.filter(id=pk).update(type_Exoneration=type, Description=des)
          return redirect('exo')
     
     return redirect('exo')

@login_required
def supexo(request):
     pk=request.POST.get("id")
     obj=Exoneration.objects.get(id=pk)
     if request.POST:
          obj.delete()
          return redirect('exo')
     return redirect('exo')
   
def register(request):
     form=Userform()
     if request.method == 'POST':
          form=Userform(data=request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, "vous avez crée un compte COTAM_Asbl avec succes")
               return redirect('connexion')
          else:
               messages.error(request, form.errors)
     return render(request, "register1.html", {'form':form, 'messages':messages})

def connexion(request):
     if request.method=="POST":
          name=request.POST['name']
          pwd=request.POST['password']
          user=authenticate(request, username=name, password=pwd)
          if user is not None and user.is_active:
               login(request, user)
               messages.success(request, "Bienvenue ")
               return redirect('index')
          else:
               messages.error(request, "Erreur d'authentification")
              
               
     return render(request, "logini.html", {'message':messages})

@login_required
def deconnexion(request):
     logout(request)
     return redirect('connexion')


def logini(request):
     return render(request, "logini.html")