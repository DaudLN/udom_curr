from django.urls import path
from .views import *


urlpatterns = [
    path('pdf', ProgramDetailView.generate_pdf, name='generate_pdf'),
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
]
