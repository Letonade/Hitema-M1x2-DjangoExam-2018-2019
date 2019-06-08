from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('calcul/<int:chiffre1>/<int:chiffre2>/<str:operator>/<str:operator>', views.home, name="core"),
    path('calcul/', views.core, name="core"),
    path('calcul/add/<int:chiffre1>/<int:chiffre2>', views.add, name = "add"),
    path('calcul/substract/<int:chiffre1>/<int:chiffre2>', views.substract, name = "substract"), 
    path('calcul/multiply/<int:chiffre1>/<int:chiffre2>', views.multiply, name = "multiply"), 
    path('calcul/divide/<int:chiffre1>/<int:chiffre2>', views.divide, name = "divide"), 
    path('calcul/load/<int:id>', views.load, name = "load"), 
 

]
