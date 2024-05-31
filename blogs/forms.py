from django import forms
from .models import UserComments

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        exclude = ["post"]
        labels = {
            "full_name" : "Name",
            "email" : "Email",
            "comment" : "Comment"
        }