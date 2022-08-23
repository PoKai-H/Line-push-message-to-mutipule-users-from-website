
from django import forms

from .models import Message,Test
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.ModelForm):

    class Meta():
        model = Message
        fields = ('__all__')
        widgets ={
            'message_push':forms.Textarea
        }

class MessageTestForm(forms.ModelForm):

    class Meta():
        model = Test
        fields = ('__all__')
        widgets ={
            'text':forms.Textarea
        }
       
#不全部以forms顯示會無法儲存