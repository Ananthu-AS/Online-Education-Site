from django import forms

from userapp.models import course, coursetype, language, price

class CourseForm(forms.ModelForm):
    class Meta:
        model = course 
        fields = ['name', 'duration', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-3'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control mt-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-3'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control mt-3'}),
        }

class LanguageForm(forms.ModelForm):
    language = forms.ModelChoiceField(
        queryset=language.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mt-3'})
    )

    class Meta:
        model = language
        fields = ['language']

class PriceForm(forms.ModelForm):
    class Meta:
        model = price 
        fields = ['price']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control mt-3'}),
        }

class CourseTypeForm(forms.ModelForm):
    type = forms.ModelChoiceField(
        queryset=coursetype.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control my-3'})
    )
    class Meta:
        model = coursetype 
        fields = ['type']



