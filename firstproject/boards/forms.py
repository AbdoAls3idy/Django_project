from  django import forms
from .models import topic,posts

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':5,
        'placeholder':'what your post',
    }),max_length=5000, help_text='The max length is 5000')
    class Meta:
        model = topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['message']