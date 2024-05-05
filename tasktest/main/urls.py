from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('show_answer/', views.show_answer, name="show_answer"),
    path('answered/', views.answered_question, name="answered_question")
]
