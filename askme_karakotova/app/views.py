from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


def paginate(request, objects_list, per_page=7):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return paginator, page_obj


def index(request):
    QUESTIONS = models.Question.objects.order_by('-add_time')
    paginator, page_obj = paginate(request, QUESTIONS, 3)
    context = {'paginator': paginator,
               'page': page_obj, 
               'popular_tags': models.Tag.objects.popular_tags,
               'best_members': models.Member.objects.best_members,
               'is_authorisated': request.user.is_authenticated}
    return render(request, 'index.html', context=context)


def login(request):
    context = {'popular_tags': models.Tag.objects.popular_tags, 
               'is_authorisated': request.user.is_authenticated,
               'best_members': models.Member.objects.best_members}
    return render(request, 'login.html', context=context)


def new_question(request):
    context = {'popular_tags': models.Tag.objects.popular_tags, 
               'is_authorisated': request.user.is_authenticated,
               'best_members': models.Member.objects.best_members}
    return render(request, 'new-question.html', context=context)


def registration(request):
    context = {'popular_tags': models.Tag.objects.popular_tags, 
               'is_authorisated': request.user.is_authenticated,
               'best_members': models.Member.objects.best_members}
    return render(request, 'registration.html', context=context)


def settings(request):
    context = {'popular_tags': models.Tag.objects.popular_tags, 
               'is_authorisated': request.user.is_authenticated,
               'best_members': models.Member.objects.best_members}
    return render(request, 'settings.html', context=context)


def question(request, id: int):
    if id <= models.Question.objects.last().id:
        question_item = models.Question.objects.get(id=id)
        paginator, page_obj = paginate(request, question_item.get_answers().order_by('-add_time'), 5)
        context = {'paginator': paginator, 
                   'page': page_obj, 
                   'question': question_item,
                   'best_members': models.Member.objects.best_members, 
                   'popular_tags': models.Tag.objects.popular_tags, 
                   'is_authorisated': request.user.is_authenticated}
        return render(request, 'question.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")


def tag(request, tag_name: str):
    if models.Tag.objects.filter(name=tag_name).count() > 0:
        tag = models.Tag.objects.get(name=tag_name)
        tag_questions = tag.questions_by_tag().order_by('-add_time')
        paginator, page_obj = paginate(request, tag_questions, 3)
        context = {'paginator': paginator, 
                   'page': page_obj, 
                   'tag': tag_name,
                   'best_members': models.Member.objects.best_members, 
                   'popular_tags': models.Tag.objects.popular_tags, 
                   'is_authorisated': request.user.is_authenticated}
        return render(request, 'tag.html', context=context)
    else:
        return HttpResponse(status=404, content="Not found")


def hot_questions(request):
    hot_questions = models.Question.objects.hot_questions()

    paginator, page_obj = paginate(request, hot_questions, 3)

    context = {'paginator': paginator, 
               'page': page_obj, 
               'popular_tags': models.Tag.objects.popular_tags,
               'best_members': models.Member.objects.best_members, 
               'is_authorisated': request.user.is_authenticated}
    return render(request, 'hot-questions.html', context=context)
        