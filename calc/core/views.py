from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .functions import *
#from .forms import ContactForm

def core(request):
	i = "0"
	if request.POST.get('operate') ==  "1":
		i="1"  
		#operation
	if request.POST.get('operate') ==  "2":
		i="2"  
		#operation
	if request.POST.get('operate') ==  "3":
		i="3"  
		#operation
	if request.POST.get('operate') ==  "4":
		i="4"  
		#operation
	if request.POST.get('operate') ==  "5":
		i="5"  
		#operation
	if request.POST.get('operate') ==  "6":
		i="6"  
		#operation
	if request.POST.get('operate') ==  "7":
		i="7"  
		#operation
	if request.POST.get('operate') ==  "8":
		i="8"  
		#operation
	if request.POST.get('operate') ==  "9":
		i="9"  
		#operation
	if request.POST.get('operate') ==  "CE":
		i="CE" 
		return redirect()
		#operation
	if request.POST.get('operate') ==  "equal":
		i="equal" 
		#operation
	if request.POST.get('operate') ==  "add":
		i="add" 
		#operation
	if request.POST.get('operate') ==  "substract":
		i="substract" 
		#operation
	if request.POST.get('operate') ==  "multiply":
		i="multiply" 
		#operation
	if request.POST.get('operate') ==  "divide":
		i="divide" 
		#operation
		test(request)
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
    




