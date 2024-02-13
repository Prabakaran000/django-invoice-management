from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.http import HttpResponseForbidden



def record(request):
    if request.method == 'POST':
        # If the request is a POST request, it means the user is trying to log in
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have logged in successfully")
            return redirect('record')  # Redirect to record page after successful login
        else:
            messages.error(request, "There was an error with your username or password")
            # Return a response even when the form is not valid
            return render(request, 'record.html', {'form': form})
    else:
        # If the request is not a POST request, it means the user is just accessing the page
        if request.user.is_authenticated:
            # If the user is authenticated, fetch records and render the record page
            records = Record.objects.all()
            return render(request, 'record.html', {'records': records})
        else:
            # If the user is not authenticated, render the login page
            form = AuthenticationForm()
            return render(request, 'record.html', {'form': form})


def home(request):
    return render(request, 'index.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')  # Redirect to record page after logout

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('record')  # Redirect to record page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def seprate(request, pk):
    if request.user.is_authenticated:
        seprate = Record.objects.get(S_No=pk)
        return render(request, 'seprate.html', {'seprate': seprate})
    else:
        messages.success(request, "You you must be login for see this page")
        return redirect('home')


def delete_record(request, pk):
    delete_it = Record.objects.get(S_No=pk)
    delete_it.delete()
    messages.success(request, "Record deleted successfully")
    return redirect('record')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully")
                return redirect('record')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(S_No=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.error(request, "Record is updated")
            return redirect('record')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')