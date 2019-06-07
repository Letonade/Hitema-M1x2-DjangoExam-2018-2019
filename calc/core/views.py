from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from core.models import equation
from .functions import *
#from .forms import ContactForm

def core(request):
	i = "0"
	#request.session['number1'] = ""
	#request.session['operation1'] = ""
	#request.session['number2'] = ""
	#request.session['operation2'] = ""
	if request.POST.get('operate') ==  "1":
		i="1"
		setNum(request, "1")  
		#operation
	if request.POST.get('operate') ==  "2":
		i="2"
		setNum(request,"2")   
		#operation
	if request.POST.get('operate') ==  "3":
		i="3"
		setNum(request,"3")   
		#operation
	if request.POST.get('operate') ==  "4":
		i="4"
		setNum(request,"4")   
		#operation
	if request.POST.get('operate') ==  "5":
		i="5"
		setNum(request,"5")   
		#operation
	if request.POST.get('operate') ==  "6":
		i="6"
		setNum(request,"6")   
		#operation
	if request.POST.get('operate') ==  "7":
		i="7"
		setNum(request,"7")   
		#operation
	if request.POST.get('operate') ==  "8":
		i="8"
		setNum(request,"8")   
		#operation
	if request.POST.get('operate') ==  "9":
		i="9"
		setNum(request,"9")   
		#operation
	if request.POST.get('operate') ==  "CE":
		i="CE" 
		CE(request)
		#operation
	if request.POST.get('operate') ==  "equal":
		i="equal" 
		if point(request) == 3:
			Iredirect = numberRedirect(request)
			if Iredirect == 0:
				return redirect(add, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 1:
				return redirect(substract, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 2:
				return redirect(multiply, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 3:
				return redirect(divide, request.session.get('number1'), request.session.get('number2'))
		#operation
	if request.POST.get('operate') ==  "add":
		i="add" 
		numberSet = setOp(request, "add")
		if numberSet == 2:
			Iredirect = numberRedirect(request)
			if Iredirect == 0:
				return redirect(add, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 1:
				return redirect(substract, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 2:
				return redirect(multiply, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 3:
				return redirect(divide, request.session.get('number1'), request.session.get('number2'))
		#operation
	if request.POST.get('operate') ==  "substract":
		i="substract"
		numberSet = setOp(request, "substract")
		if numberSet == 2:
			Iredirect = numberRedirect(request)
			if Iredirect == 0:
				return redirect(add, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 1:
				return redirect(substract, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 2:
				return redirect(multiply, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 3:
				return redirect(divide, request.session.get('number1'), request.session.get('number2')) 
		#operation
	if request.POST.get('operate') ==  "multiply":
		i="multiply" 
		numberSet = setOp(request, "multiply")
		if numberSet == 2:
			Iredirect = numberRedirect(request)
			if Iredirect == 0:
				return redirect(add, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 1:
				return redirect(substract, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 2:
				return redirect(multiply, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 3:
				return redirect(divide, request.session.get('number1'), request.session.get('number2'))
		#operation
	if request.POST.get('operate') ==  "divide":
		i="divide" 
		numberSet = setOp(request, "divide")
		if numberSet == 2:
			Iredirect = numberRedirect(request)
			if Iredirect == 0:
				return redirect(add, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 1:
				return redirect(substract, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 2:
				return redirect(multiply, request.session.get('number1'), request.session.get('number2'))
			if Iredirect == 3:
				return redirect(divide, request.session.get('number1'), request.session.get('number2'))
		#operation
		point(request)

	number1 = request.session.get('number1');
	operation1 = request.session.get('operation1');
	if operation1 == "add" : operation1 = "+"
	if operation1 == "substract" : operation1 = "-"
	if operation1 == "divide" : operation1 = "/"
	if operation1 == "multiply" : operation1 = "x"
	number2 = request.session.get('number2');
	equations = equation.objects.all()
	return render(request, 'core/core.html', locals())
    

def add(request, chiffre1 ,chiffre2):
	
	total = int(chiffre1) + int(chiffre2)
	equation(chiffre1 = request.session.get('number1'), operation = request.session.get('operation1'), chiffre2 = request.session.get('number2')).save()
	request.session['operation1'] = ""
	if request.session.get('operation2') != "":
		request.session['operation1'] = request.session.get('operation2') 
	request.session['operation2'] = ""
	request.session['number1'] = str(total)
	request.session['number2'] = ""	
	return redirect(core)
    

def substract(request, chiffre1 ,chiffre2):
	
	total = int(chiffre1) - int(chiffre2)
	request.session['operation1'] = ""
	if request.session.get('operation2') != "":
		request.session['operation1'] = request.session.get('operation2') 
	request.session['operation2'] = ""
	request.session['number1'] = str(total)
	request.session['number2'] = ""	
	return redirect(core)
    

def multiply(request, chiffre1 ,chiffre2):
	
	total = int(chiffre1) * int(chiffre2)
	request.session['operation1'] = ""
	if request.session.get('operation2') != "":
		request.session['operation1'] = request.session.get('operation2') 
	request.session['operation2'] = ""
	request.session['number1'] = str(total)
	request.session['number2'] = ""	
	return redirect(core)
    

def divide(request, chiffre1 ,chiffre2):
	
	total = int(chiffre1) / int(chiffre2)
	request.session['operation1'] = ""
	if request.session.get('operation2') != "":
		request.session['operation1'] = request.session.get('operation2') 
	request.session['operation2'] = ""
	request.session['number1'] = str(total)
	request.session['number2'] = ""	
	return redirect(core)
    




