from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder' : 'Enter the content',
                'rows' :5,
                'cols' :50,
                
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)   
        # exclude = ('title',)