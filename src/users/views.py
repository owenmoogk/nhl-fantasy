from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from .forms import EditProfileForm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": UserCreationForm})

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home/")
        else:
            event = form.cleaned_data
            if event.get("password1") != event.get("password2"):
                errorMsg = "Passwords do not match"
            else:
                errorMsg = "Username already exists"
            context = {
                "form": UserCreationForm,
                "error": errorMsg
            }
            return render(request, "users/register.html", context)

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/home/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change-password.html', {'form': form})

@login_required
def account(request):

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = EditProfileForm(instance = request.user)
    
        return render(request, "users/account.html", {"form": form})


def homeView(request):
    return render(request, "home.html", {})