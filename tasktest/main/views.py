from django.shortcuts import render
from .models import TestQuestions
from random import randint

question_number = 1


def index(request):
    global question_number
    question_number = randint(1, 100)
    question = TestQuestions.objects.get(number=question_number)
    return render(request, 'main/index.html', {'question': question})


def show_answer(request):
    global question_number
    question = TestQuestions.objects.get(number=question_number)
    return render(request, 'main/show_answer.html', {'question': question})


def answered_question(request):
    global question_number
    answer = request.POST['answer']
    question = TestQuestions.objects.get(number=question_number)
    if answer == question.answer:
        return render(request, 'main/answered_question.html', {'result': '✅', 'question': question})
    return render(request, 'main/answered_question.html', {'result': '❌', 'question': question})
