from apps.customers.views import leads

from django.urls import path

app_name = 'customers'
urlpatterns = [
    # Leads
    path('leads/create',
         leads.LeadCreateView.as_view(),
         name='lead_create'),
    path('leads/',
         leads.LeadListView.as_view(),
         name='lead_list'),
    path('leads/<int:pk>/update/',
         leads.LeadUpdateView.as_view(),
         name='lead_update'),
    path('leads/<int:pk>/delete/',
         leads.LeadDeleteView.as_view(),
         name='lead_delete'),
    path('leads/<int:pk>/',
         leads.LeadDetailView.as_view(),
         name='lead_detail'),
]
