from django import forms
from .models import Article
 
# class AriticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea(
#         attrs={
#             'placeholder' : 'Enter the content'
#         }
#     ))

class AriticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'