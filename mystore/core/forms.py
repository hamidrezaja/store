from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment_content']
        widgets = {
            'comment_content': forms.Textarea(attrs={'placeholder': 'نظر شما....', 'rows': 4}),
        }