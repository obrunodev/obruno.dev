from apps.customers.models import Lead

from django import forms


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ['company_name', 'contact_name', 'niche', 'phone_number',
                  'has_whatsapp', 'website_link', 'lead_origin',
                  'contact_status']
