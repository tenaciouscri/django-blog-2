from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "title_tag",
            "body",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title..."}
            ),
            "title_tag": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title Tag..."}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Body..."}
            ),
        }
