from django import forms
from django.forms import ModelForm
from .models import Articles

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Articles.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Please pick another title.")
        return data