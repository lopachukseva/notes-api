from django.urls import path

from api import views

urlpatterns = [
    path("api/notes/", views.NoteAPIList.as_view()),
    path("api/notes/<int:pk>", views.NoteAPIDetailView.as_view()),
]
