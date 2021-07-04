from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import patients
from .models import test
from .models import vac
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from covid.settings import EMAIL_HOST_USER
@login_required
def home(request):
	return render(request,'index.html')
def loginview(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)
		return redirect('home')
	else:
		return render(request,'login.html')
def logout_view(request):
	logout(request)
	return redirect('login')
def sign_up(request):
	form=UserCreationForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/sign_up.html',{'form':form})
def Resethome(request):
	return render(request,'registration/ResetPassword.html')

def resetPassword(request):
	responseDic={}
	try:
		username=request.POST['uname']
		print(username)
		recepient=request.POST['email']
		print(recepient)
		pwd=request.POST['password']
		print(pwd)
		subject='Password reset'
		try:
			user=User.objects.get(username=username)
			if user is not None:
				user.set_password(pwd)
				user.save()
				message='Your password was changed'
				send_mail(subject,message,EMAIL_HOST_USER,[recepient])
				responseDic['errmsg']='Password Reset Successfully'
				return render(request,'registration/ResetPassword.html',responseDic)
		except Exception as e:
			print(e)
			responseDic['errmsg']='Email doesnt Exist'
			return render(request,'registration/ResetPassword.html',responseDic)
	except Exception as e:
			print(e)
			responseDic['errmsg']='Failed to reset password'
			return render(request,'registration/ResetPassword.html',responseDic)
def display(request):
	pdtls=patients.objects.all()
	print(pdtls)
	return render(request,'patients.html',{'pdtls':pdtls})
def display1(request):
	tdtls=test.objects.all()
	print(tdtls)
	return render(request,'test.html',{'tdtls':tdtls})
def vaccine(request):
	adharnum=request.POST['anum']
	name=request.POST['name']
	gender=request.POST['gender']
	dob=request.POST['dob']
	vc=vac(adharnum=adharnum,name=name,gender=gender,dob=dob)
	vc.save()
	return render(request,'index.html')

	
# Create your views here.

# Create your views here.
