from apps.customers.forms import LeadForm
from apps.customers.models import Lead

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)

SUCCESS_URL = reverse_lazy('customers:lead_list') 


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead 
    template_name = 'customers/leads/lead_form.html'
    form_class = LeadForm
    success_url = SUCCESS_URL


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'customers/leads/lead_list.html'
    context_object_name = 'leads'


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'customers/leads/lead_detail.html'
    context_object_name = 'lead'


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    template_name = 'customers/leads/lead_form.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse_lazy('customers:lead_detail',
                            kwargs={'pk': self.object.pk}) 


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    template_name = 'customers/leads/lead_confirm_delete.html'
    success_url = SUCCESS_URL
