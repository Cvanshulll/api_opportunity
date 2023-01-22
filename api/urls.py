from django.urls import path
from api import views


urlpatterns = [
    path('', views.OpportunityListView.as_view()),
]