from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(max_length=35)
    group = forms.IntegerField()

class StudentForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()

class ProfessorForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=35)
    email = forms.EmailField()
    profession = forms.CharField(max_length=30)
