from django import forms
from taggit.forms import TagField
from django_select2.forms import Select2TagWidget
from .models import Service

class ServiceForm(forms.ModelForm):
    tags = TagField(
        widget=Select2TagWidget(attrs={"data-tags": "true"}),
        required=False
    )

    class Meta:
        model = Service
        fields = '__all__'

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', [])
        total_length = sum(len(tag) for tag in tags)
        if total_length > 200:
            raise forms.ValidationError("Total length of all tags must not exceed 200 characters.")
        return tags
