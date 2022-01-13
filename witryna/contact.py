from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'firstname', 'placeholder': 'Firstname'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'surname', 'placeholder': 'Surname'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'subject', 'placeholder': 'Subject'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'rows': '7', 'cols': '50'}))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        firstname = cleaned_data.get('firstname')
        surname = cleaned_data.get('surname')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not firstname and not surname and not email and not subject and not message:
            raise forms.ValidationError('You have to write something!')
