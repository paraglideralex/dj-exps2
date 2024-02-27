from django.urls import path
from SurveyApp import views

urlpatterns = [
    path("", views.customer, name="customer"),  

]