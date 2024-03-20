from django import forms
from .models import Thesis, ResearchPaper, ResearchData



class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'description', 'file']

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'description', 'file']
        
class ResearchDataForm(forms.ModelForm):
    class Meta:
        model = ResearchData
        fields = ['title', 'data_file']