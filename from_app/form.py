from django import forms
from from_app.models import Form


class Forms(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
