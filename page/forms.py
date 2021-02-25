from django import forms
from page.models import FreeFireAccount

class FreeFireAccountform(forms.ModelForm):
    email_username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    class Meta:
        model = FreeFireAccount
        fields = ('email_username', 'password')
    

    def clean_email_username(self):
        email_username = self.cleaned_data["email_username"].lower()
        try:
            account = FreeFireAccount.objects.get(email_username=email_username)
        except Exception as e:
            return email_username
        raise forms.ValidationError(f'Email or Phone number {email_username} alredy use')

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password too short.')
        return password
        