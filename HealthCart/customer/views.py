from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .forms import *
class CustomerSignup(View):
    def get(self,request):
        return render(request,'customer/signup.html')
    def post(self,request):
        data=request.POST
        print(data)
        myform=MyUserForm(data=data)
        if myform.is_valid():
            myform.save()
            return redirect("log-in")
        else:
            return HttpResponse(myform.errors)
class Customerlogin(View):
    def get(self,request):
        return render(request,'customer/login.html')
