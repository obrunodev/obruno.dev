from apps.notes import views

from django.urls import path

app_name = 'notes'
urlpatterns = [
    path('create/', views.notes_create, name='create'),
    path('', views.notes_list, name='list'),
    path('<int:note_id>/update/', views.notes_update, name='update'),
    path('<int:note_id>/delete/', views.notes_delete, name='delete'),
    path('<int:note_id>/detail/', views.notes_detail, name='detail'),
]
