from django import forms
from page.models import FreeFireAccount

class FreeFireAccountform(forms.ModelForm):
    class Meta:
        model = FreeFireAccount
        fields = ('email_username', 'password')