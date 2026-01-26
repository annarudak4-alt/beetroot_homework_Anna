from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']
        # Додамо стилі Bootstrap або звичайні класи для краси
        widgets = {
            'reminder': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }