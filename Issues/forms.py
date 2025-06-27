from django.forms import ModelForm
from .models import *

class Issue_Form(ModelForm):
    
    class Meta:
        model=Issues
        fields=["title","description","status","priority"]