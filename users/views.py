from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm -- default user creation form by django
from .forms import RegisterForm # newly modified form by user by adding email field in the existing form.
from django.contrib import messages
# Create your views here.

def register(request):
    print(request.method)
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            # print("yes")
            form.save()
            userform=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {userform}, your account has been created succussfully')
            return redirect('food:login')
        
    else:
        form =RegisterForm()
    return render(request, 'users/register.html',{'form':form})
@login_required
def profilepage(request):
    return render(request,'users/profile.html')