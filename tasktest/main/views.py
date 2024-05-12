from django.shortcuts import render
from .models import TestQuestions, UsersQuestionTables
from random import randint


def index(request):
    question_count = len(TestQuestions.objects.all())
    question_number = randint(1, question_count)

    current_user_ip_address = request.META['REMOTE_ADDR']

    try:
        user = UsersQuestionTables.objects.get(user_ip=current_user_ip_address)
        user.current_question = question_number
        user.save()
    except Exception as e:
        UsersQuestionTables.objects.create(user_ip=current_user_ip_address, current_question=question_number)

    question = TestQuestions.objects.get(id=question_number)
    return render(request, 'main/index.html', {'question': question})


def show_answer(request):
    current_user_ip_address = request.META['REMOTE_ADDR']
    user = UsersQuestionTables.objects.get(user_ip=current_user_ip_address)
    question_number = user.current_question

    question = TestQuestions.objects.get(id=question_number)
    return render(request, 'main/show_answer.html', {'question': question})


def answered_question(request):
    current_user_ip_address = request.META['REMOTE_ADDR']
    user = UsersQuestionTables.objects.get(user_ip=current_user_ip_address)
    question_number = user.current_question

    answer = request.POST['answer']
    question = TestQuestions.objects.get(id=question_number)
    if answer.strip().lower() == question.answer.strip().lower():
        return render(request, 'main/answered_question.html', {'result': '✅', 'question': question})
    return render(request, 'main/answered_question.html', {'result': '❌', 'question': question})
