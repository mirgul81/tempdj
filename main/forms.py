from django import forms
from .models import Regions
from .models import Areas


class CreateRegionForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = "__all__"


class CreateAreaForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = "__all__"