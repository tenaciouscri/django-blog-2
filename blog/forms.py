from django import forms

from .models import Category, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "title_tag",
            "category",
            "body",
        ]

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title here..."}))
    title_tag = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title tag here..."}))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your post here..."}))
