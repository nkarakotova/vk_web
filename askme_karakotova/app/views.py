from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'login.html')


def new_question(request):
	return render(request, 'new-question.html')


def question(request, question_id: int):
	question_item = models.QUESTIONS[question_id]
	answer_item = models.ANSWERS
	context = {'question': question_item, 'answers': answer_item}
	return render(request, 'question.html', context=context)


def registration(request):
	return render(request, 'registration.html')


def settings(request):
	return render(request, 'settings.html')


def tag(request):
	context = {'questions': models.QUESTIONS}
	return render(request, 'tag.html', context=context)

