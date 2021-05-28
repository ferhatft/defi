from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminiz'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail Adresiniz'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınız'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
