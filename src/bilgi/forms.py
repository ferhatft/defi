from django import forms
from django.forms import inlineformset_factory
from .widgets import CustomClearableFileInput

from .models import İnformationModel, AnswerinlineModel


class İnformationForm(forms.ModelForm):
    class Meta:
        model = İnformationModel
        fields = ['title', 'tags', 'backimage', 'intro']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'medium-input',
                'placeholder': 'Başlık',
            }),
            # 'tags': forms.TextInput(attrs={
            # 'class': 'medium-input',
            # 'placeholder': 'Tag.. "spor,resim,üniversite,..." ',
            # }),
        }

        labels = {
            "main_context": "",
            "title": "",
            "backimage":"asfasfsa"
        }

    backimage = forms.FileField(
        label='Gerber', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'tags':
                self.fields[field].widget.attrs['placeholder'] = 'Tag.. "spor,resim,üniversite,..." '
           

            # if field == 'backimage':

                # self.fields[field].widget.attrs['class'] = 'btn btn-medium btn-dark-gray lg-margin-15px-bottom d-table d-lg-inline-block md-margin-lr-auto'

                # self.fields[field].widget.attrs['accept'] = '.zip , .rar'

                # <a class = "btn btn-medium btn-dark-gray lg-margin-15px-bottom d-table d-lg-inline-block md-margin-lr-auto" href = "#" > Button Medium < /a >


class AnswerinlineModelForm(forms.ModelForm):
    class Meta:
        model = AnswerinlineModel
        fields = ['main_context', ]
        widgets = {
            'main_context': forms.Textarea(attrs={
                'class': 'medium-textarea',
                'placeholder': 'Görüşünüzü Girin',
                'rows': "8",
                'cols': '200',
            }),
        }

        labels = {
            "main_context": ""
        }

        # def __init__(self, *args, **kwargs):
        #     super(DictionaryForm, self).__init__(*args, **kwargs)
        #     for visible in self.visible_fields():
        #         visible.field.widget.attrs['class'] = 'form-control'
