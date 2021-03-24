from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):
    
    # overriding the password form just cuz i dont want it
    password = None

    class Meta:
        model = User

        # you can make a fields list of fields ot include or a exlude list of fields to not include

        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )