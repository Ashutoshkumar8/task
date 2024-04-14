from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,'add_task.html')

def add_user(req):
    if(req.method=='GET'):
        return render(req,'add_user.html')
    else:
        name=req.POST.get('name')
        email=req.POST.get('email')
        phone=req.POST.get('mobile')
        obj=Signup(name=name,email=email,mobile=mobile)
        obj.save()
        return redirect()

