from django.urls import path

from . import views

urlpatterns = [
    path("", views.getRecords, name="get-records"),
    path("add/", views.addRecord, name="add-record"),
]
