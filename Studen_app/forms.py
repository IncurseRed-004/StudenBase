from django import forms

from Studen_app.models import Students


class studentForm(forms.ModelForm):
    class Meta:
        model =Students
        fields =['name','age',"email","phone",'course']
