from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from .models import User, Student, College, Government
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import StudentForm, CollegeForm, UserForm
# Create your views here.
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = StudentForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return render(request,'portal/login.html',{})

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = StudentForm()

    return render(request,'portal/signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def register1(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = CollegeForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return render(request,'portal/login.html',{})
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CollegeForm()

    return render(request,'portal/signup1.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username ,password = password)
        login_user = False
        if user:
            if user.is_active:
                login(request,user)
            else:
                return HttpResponse("Account Not active")
        else:
            login_user = True
            return render(request,'portal/login.html',{'login_user':login_user})

    else:
        return render(request,'portal/login.html',{})
