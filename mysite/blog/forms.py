from django import forms
from blog.models import Post,Comment
#2 Forms for the 2 Models i.e PostForm and CommentForm


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')#Fields that are needed to be modified!

        #widgets are used to style these particular components used here using CSS
    widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
    }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

    widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
    }
