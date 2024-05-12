from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('show_answer/<int:id>', views.show_answer, name="show_answer"),
    path('answered/<int:id>', views.answered_question, name="answered_question")
]
