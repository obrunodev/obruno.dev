from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = [
            'company_name', 'contact_name', 'niche', 'phone_number',
            'has_whatsapp', 'website_link', 'lead_origin',
            'contact_status', 'return_date', 'observations',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'niche': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'website_link': forms.TextInput(attrs={'class': 'form-control'}),
            'lead_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_status': forms.Select(attrs={'class': 'form-select'}),
            'has_whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'return_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'observations': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs['placeholder'] = 'Nome da Empresa'
        self.fields['contact_name'].widget.attrs['placeholder'] = 'Nome do Contato'
