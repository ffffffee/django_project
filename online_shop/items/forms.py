from django import forms
from .models import AddUser,Items,Producer

class AddUserForm(forms.ModelForm):
   class Meta:
      model=AddUser
      fields='__all__'

class AddItemForm(forms.ModelForm):
   class Meta:
      model = Items
      fields = '__all__'

class AddProduser(forms.ModelForm):
   class Meta:
      model = Producer
      fields = '__all__'