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

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    title_tag = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
