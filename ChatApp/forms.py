from django.forms import ModelForm
from django import forms
from .models  import *
class ChatMessagesCreateForm(forms.ModelForm):
    class Meta:
        model=GroupMessages
        fields=['body']
        widgets={
            'body':forms.TextInput(attrs={'placeholder':'Add messages ...','class':'p-4 text-black','max_length':'300','auto_focus':True})
        }
