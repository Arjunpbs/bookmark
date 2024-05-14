from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from book.models import Contactus
# Create your views here.
def index(request):
   	return render(request,"index.html")
def signin(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['pass1']
		confirm_password=request.POST['pass2']
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		if password != confirm_password:
			messages.error(request,"passwords Are Not Matching")
			return render(request,"signin.html")
		try:
			if User.objects.get(username=email):
				messages.error(request,"This Email Already Exists")
				return render(request,"signin.html")
		except Exception as identifier:
			pass
		user = User.objects.create_user(email,email,password)
		user.save()
		messages.warning(request,"Signin Completed")
		return render(request,"index.html")
	return render(request,"signin.html")

def handlelogin(request):
	if request.method=="POST":
		username=request.POST['email']
		userpassword=request.POST['pass1']
		myuser=authenticate(username=username,password=userpassword)
		if myuser is not None:
			login(request,myuser)
			messages.success(request,"Login Successfull")
			return render(request,"index.html")
		else:
			messages.error(request,"Email or Password is Invalid")
			return render(request,"login.html")
	return render(request,"login.html")

def handlelogout(request):
	logout(request)
	messages.success(request,"Successfully Logout")
	return render(request,"index.html")
		
def getstarted(request):
	if request.user.is_authenticated:
		return render(request,"interior2.html")
	else:
		messages.warning(request,"Login first")
		return render(request,"index.html")

def contact(request):
	if request.method=="POST":
		name=request.POST['name']
		mobnumber=request.POST['mobnumber']
		subject=request.POST['subject']
		message=request.POST['message']
		obcontact=Contactus(name=name,phoneno=mobnumber,subject=subject,message=message)
		obcontact.save()
		messages.success(request,"Complaint send Successfully")
		return render(request,"index.html")
		


	
		
	   	
		


