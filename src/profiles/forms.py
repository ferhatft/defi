from django import forms
from .models import UserProfile
from .widgets import CustomClearableFileInput

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['abaout','profileimage']
        widgets = {
            'abaout': forms.Textarea(attrs={
                'class': 'medium-textarea',
                'placeholder': 'Hakkımda',
                'rows': "8",
                'cols': '100',
            }),
        }

        labels = {
            "main_context": "",
            "title":"",
        }
    
    profileimage = forms.FileField(
        label='resim', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'tags' :
                self.fields[field].widget.attrs['placeholder'] ='Tag.. "spor,resim,üniversite,..." '
            
