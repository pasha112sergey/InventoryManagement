from django.forms import ModelForm
from .models import Inventory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']

class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
