from django.urls import path

from . import views

urlpatterns = [
    path('views/', views.NoteList.as_view(), name='notes'),
    path('<int:pk>/', views.NoteDetail.as_view())  # api/vl/notes/1
]
