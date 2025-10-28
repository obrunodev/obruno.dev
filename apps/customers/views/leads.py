from apps.customers.forms import LeadForm
from apps.customers.models import Lead

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Case, When, Value, IntegerField
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)

SUCCESS_URL = reverse_lazy('customers:lead_list') 

STATUS_ORDER = [
    Lead.LeadStatusChoices.NEW,
    Lead.LeadStatusChoices.PENDING,
    Lead.LeadStatusChoices.ATTEMPTING_CONTACT,
    Lead.LeadStatusChoices.IN_CONTACT,
    Lead.LeadStatusChoices.QUALIFIED,
    Lead.LeadStatusChoices.DEVELOPMENT,
    Lead.LeadStatusChoices.PROPOSAL_SENT,
    Lead.LeadStatusChoices.ON_HOLD_SCHEDULED,
    Lead.LeadStatusChoices.CLOSED,
    Lead.LeadStatusChoices.UNQUALIFIED,
]


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead 
    template_name = 'customers/leads/lead_form.html'
    form_class = LeadForm
    success_url = SUCCESS_URL


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'customers/leads/lead_list.html'
    context_object_name = 'leads'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        
        ordering_cases = [
            When(contact_status=status_code, then=Value(index))
            for index, status_code in enumerate(STATUS_ORDER)
        ]
        
        qs = qs.annotate(
            order_rank=Case(
                *ordering_cases,
                default=Value(len(STATUS_ORDER)),
                output_field=IntegerField()
            )
        )
        
        qs = qs.order_by('order_rank', 'company_name')
        
        if q := self.request.GET.get('q'):
            qs = qs.filter(
                Q(company_name__icontains=q) |
                Q(contact_name__icontains=q) |
                Q(niche__icontains=q)
            )
        
        if f := self.request.GET.get('f'):
            qs = qs.filter(contact_status=f)
        
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads_count'] = Lead.objects.count()
        return context


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
