from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import  SignUpForm



# Create your views here.

def home(request):

    records = Record.objects.all()

    # Check to see if logged

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            messages.success(request, "You are logged")

            return redirect('home')
        else:

            messages.success(request, "There's something missing!!")
            return redirect('home')
    else:        
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    
    logout(request)
    messages.success(request,'You have been logged out...')    
    return redirect('home')

def register(request):
    
    if request.method == 'POST':

        form = SignUpForm(request.POST)
         
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, 'You are here')
            return redirect('home')
        
    else:

        form = SignUpForm
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
            messages.success(request, 'Logged....')
            return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_id = Record.objects.get(id=pk)
        delete_id.delete()
        messages.success(request, 'Gone, reduced to atoms....')
        return redirect('home')
    else:
        return redirect('home')