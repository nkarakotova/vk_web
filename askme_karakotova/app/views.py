from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


def index(request):
    paginator = Paginator(models.QUESTIONS, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'paginator': paginator, 
               'page': page_obj, 
               'popular_tags': models.POPULAR_TAGS, 
               'is_authorisated': models.IS_AUTHORISATED,
               'best_members': models.BEST_MEMBERS}

    return render(request, 'index.html', context=context)


def login(request):
    context = {'popular_tags': models.POPULAR_TAGS, 
               'is_authorisated': models.IS_AUTHORISATED,
               'best_members': models.BEST_MEMBERS}
    return render(request, 'login.html', context=context)


def new_question(request):
    context = {'popular_tags': models.POPULAR_TAGS, 
               'is_authorisated': models.IS_AUTHORISATED,
               'best_members': models.BEST_MEMBERS}
    return render(request, 'new-question.html', context=context)


def question(request, question_id: int):
    if question_id < len(models.QUESTIONS):
        question_item = models.QUESTIONS[question_id]
        paginator = Paginator(question_item['answers'], 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {'paginator': paginator, 
                   'page': page_obj, 
                   'popular_tags': models.POPULAR_TAGS, 
                   'is_authorisated': models.IS_AUTHORISATED,
                   'best_members': models.BEST_MEMBERS,
                   'question_item': question_item}
        return render(request, 'question.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")


def registration(request):
    context = {'popular_tags': models.POPULAR_TAGS, 
               'is_authorisated': models.IS_AUTHORISATED,
               'best_members': models.BEST_MEMBERS}
    return render(request, 'registration.html', context=context)


def settings(request):
    context = {'popular_tags': models.POPULAR_TAGS, 
               'is_authorisated': models.IS_AUTHORISATED,
               'best_members': models.BEST_MEMBERS}
    return render(request, 'settings.html', context=context)


def tag(request, question_tag: str):
    tag_questions = []
    for question_item in models.QUESTIONS:
        if question_tag in question_item['tags']:
            tag_questions.append(question_item)

    if len(tag_questions) > 0:
        paginator = Paginator(tag_questions, 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {'paginator': paginator, 
                   'page': page_obj, 
                   'tag': question_tag,
                   'best_members': models.BEST_MEMBERS, 
                   'popular_tags': models.POPULAR_TAGS, 
                   'is_authorisated': models.IS_AUTHORISATED}
        return render(request, 'tag.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")
