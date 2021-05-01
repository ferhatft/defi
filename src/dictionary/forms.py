from django import forms
from .models import DictionaryModel, AnswerinlineModel,ReporModel


class DictionaryForm(forms.ModelForm):
    class Meta:
        model = DictionaryModel
        fields = ['title','tags','main_context',]
        widgets = {
            'main_context': forms.Textarea(attrs={
                'class': 'medium-textarea',
                'placeholder': 'Görüşünüzü Girin',
                'rows': "8",
                'cols': '100',
            }),

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
            "title":"",
        }
        
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'tags' :
                self.fields[field].widget.attrs['placeholder'] ='Tag.. "spor,resim,üniversite,..." '
            



class AnswerinlineModelForm(forms.ModelForm):
    class Meta:
        model = AnswerinlineModel
        fields = ['main_context', ]
        widgets = {
            'main_context': forms.Textarea(attrs={
                'class': 'medium-textarea',
                'placeholder': 'Görüşünüzü Girin',
                'rows': "8",
                'cols': '100',
            }),
        }

        labels = {
            "main_context": ""
        }

    
        # def __init__(self, *args, **kwargs):
        #     super(DictionaryForm, self).__init__(*args, **kwargs)
        #     for visible in self.visible_fields():
        #         visible.field.widget.attrs['class'] = 'form-control'


class ReportModelForm(forms.ModelForm):
    class Meta:
        model = ReporModel
        fields = ['main_context', ]
        widgets = {
            'main_context': forms.Textarea(attrs={
                'class': 'medium-textarea',
                'placeholder': 'Görüşünüzü Girin',
                'rows': "8",
                'cols': '100',
            }),
        }

        labels = {
            "main_context": ""
        }

    
        # def __init__(self, *args, **kwargs):
        #     super(DictionaryForm, self).__init__(*args, **kwargs)
        #     for visible in self.visible_fields():
        #         visible.field.widget.attrs['class'] = 'form-control'

