from django.shortcuts import render
from .models import TestQuestions, Users
from random import randint
from django.core.cache import cache


def index(request):
    question_count = len(TestQuestions.objects.all())
    question_number = randint(1, question_count)
    current_user = request.user.id

    if Users.objects.get(user_id=current_user):
        user = Users.objects.get(user_id=current_user)
        user.current_question = question_number
        user.save()
    else:
        Users.objects.create(user_id=current_user, current_question=question_number)

    question = TestQuestions.objects.get(id=question_number)
    return render(request, 'main/index.html', {'question': question})


def show_answer(request):
    current_user = request.user.id
    user = Users.objects.get(user_id=current_user)
    question_number = user.current_question

    question = TestQuestions.objects.get(id=question_number)
    return render(request, 'main/show_answer.html', {'question': question})


def answered_question(request):
    current_user = request.user.id
    user = Users.objects.get(user_id=current_user)
    question_number = user.current_question

    answer = request.POST['answer']
    question = TestQuestions.objects.get(id=question_number)
    if answer.strip().lower() == question.answer.strip().lower():
        return render(request, 'main/answered_question.html', {'result': '✅', 'question': question})
    return render(request, 'main/answered_question.html', {'result': '❌', 'question': question})
