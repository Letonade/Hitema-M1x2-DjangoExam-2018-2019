from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
#from .forms import ContactForm

def core(request):

	return render(request, 'core/core.html', locals())
    

def add(request, chiffre1 ,chiffre2):
	chiffre1=1
	chiffre2=2
	return render(request, 'core/core.html', locals())
    

def substract(request, chiffre1 ,chiffre2):
	chiffre1=1
	chiffre2=2
	return render(request, 'core/core.html', locals())
    

def multiply(request, chiffre1 ,chiffre2):
	chiffre1=1
	chiffre2=2
	return render(request, 'core/core.html', locals())
    

def divide(request, chiffre1 ,chiffre2):
	chiffre1=1
	chiffre2=2
	return render(request, 'core/core.html', locals())
    




