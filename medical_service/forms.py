from django import forms  
from medical_service.models import *
class CountryForm(forms.ModelForm):  
    class Meta:  
        model = Country
        fields = "__all__"  

class DiseaseTypeForm(forms.ModelForm):  
    class Meta:  
        model = Diseasetype
        fields = "__all__"  

class DiseaseForm(forms.ModelForm):  
    class Meta:  
        model = Disease
        fields = "__all__"  

class DiscoverForm(forms.ModelForm):  
    class Meta:  
        model = Discover
        fields = "__all__"

class UsersForm(forms.ModelForm):  
    class Meta:  
        model = Users
        fields = "__all__"

class PublicForm(forms.ModelForm):  
    class Meta:  
        model = Publicservant
        fields = "__all__"
    
class DoctorForm(forms.ModelForm):  
    class Meta:  
        model = Doctor
        fields = "__all__"
    
class SpecForm(forms.ModelForm):  
    class Meta:  
        model = Specialize
        fields = "__all__"

class RecordForm(forms.ModelForm):  
    class Meta:  
        model = Record
        fields = "__all__"