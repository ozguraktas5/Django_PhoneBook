from django import forms
from .models import Person, Category, Location

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'image', 'address', 'categories']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "required": "required"}),
            "last_name" : forms.TextInput(attrs={"class": "form-control", "required": "required"}),
            "phone_number" : forms.TextInput(attrs={"class": "form-control", "required": "required"}),
            "email" : forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
            "image" : forms.FileInput(attrs={"class": "form-control", "required": "required"}),
            "address" : forms.TextInput(attrs={"class": "form-control", "required": "required"}),
            "categories" : forms.SelectMultiple(attrs={"class": "form-control", "required": "required"}),    
        }
        
    
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "required": "required"}),
               
        }
        
class LocationForm(forms.ModelForm):
      class Meta:
          model = Location
          fields = ['city', 'neighbourhood']
          widgets = {
              "city": forms.TextInput(attrs={"class": "form-control", "required": "required"}),
              "neighbourhood": forms.TextInput(attrs={"class": "form-control", "required": "required"}),
               
          }

class UploadForm(forms.Form):
    image = forms.ImageField()