from django.urls import path
from .views import HomeView, ProjectDetailView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
