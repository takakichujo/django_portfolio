from django import forms
from .models import Testlist


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Testlist
        fields = ["id","name","age","email","prefecture_no","prefecture_name","prefecture_kana"],