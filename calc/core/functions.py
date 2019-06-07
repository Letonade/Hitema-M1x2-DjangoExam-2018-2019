from datetime import datetime

def point(request):
	#print(request.session.get('number1'))
	if request.session.get('number2') != "":
		return 3
	if request.session.get('operation1') != "":
		return 2
	if request.session.get('number1') != "":
		return 1
	return 0


def setNum(request, val):
	Ipoint = point(request)
	if Ipoint == 0:
		request.session['number1']=val
		print(Ipoint)
		return 0
	if Ipoint == 1:
		request.session['number1']+=val
		print(Ipoint)
		return 0
	if Ipoint == 2:
		request.session['number2']=val
		print(Ipoint)
		return 0
	if Ipoint == 3:
		request.session['number2']+=val
		print(Ipoint)
		return 0
	return 1

def setOp(request, val):
	Ipoint = point(request)
	if Ipoint == 0:
		print(Ipoint)
		return 1
	if Ipoint == 1:
		print(Ipoint)
		request.session['operation1']=val
		return 1
	if Ipoint == 2:
		print(Ipoint)
		return 1
	if Ipoint == 3:
		print(Ipoint)
		request.session['operation2']=val
		return 2
	return 0

def numberRedirect(request):
	operation = request.session.get('operation1')
	print('numberRedirect')
	print(operation)
	if operation == "add":
		print(0)
		return 0
	if operation == "substract":
		print(1)
		return 1
	if operation == "multiply":
		print(2)
		return 2
	if operation == "divide":
		print(3)
		return 3

def CE(request):
	request.session['number1'] = ""
	request.session['operation1'] = ""
	request.session['number2'] = ""
	request.session['operation2'] = ""

	