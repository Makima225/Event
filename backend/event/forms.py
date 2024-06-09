from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'surname', 'residence', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Surname'}),
            'residence': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Residence'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone'}),
        }

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''    