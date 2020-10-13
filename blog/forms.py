from django import forms
from django.forms import ModelForm
from .models import BlogPost



class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content','publish_date']


    def clean_title(self,*args,**kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("title already exists")
        return title

