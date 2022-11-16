from django.db import models
from django.contrib.auth.models import User
import django.contrib.auth.backends
import os.path
from django.db.models import Count
from django.db.models import Sum

class MemberManager(models.Manager):
    def best_members(self):
        return self.all().annotate(rating=Count('questions')).order_by('rating').reverse()[:5]


class Member(models.Model):
    info = models.OneToOneField(django.contrib.auth.backends.UserModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default="static/img/korgi.jpg", upload_to="app/static/img", blank=True)

    objects = MemberManager()

    def get_avatar(self):
        return "img/" + os.path.basename(self.avatar.name)

    def rating(self) -> int:
        return self.questions.agregate(Sum('rating')) + self.answers.agregate(Sum('rating'))

    def __str__(self):
        return self.info.__str__()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.all().annotate(rating=Count('like_users') - Count('dislike_users')).order_by('rating').reverse()[:5]

class Question(models.Model):
    title = models.CharField(max_length=77, unique=True)
    text = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="questions")
    like_users = models.ManyToManyField(Member, related_name="question_likes", blank=True)
    dislike_users = models.ManyToManyField(Member, related_name="question_dislikes", blank=True)

    objects = QuestionManager()

    def get_text(self):
        return self.text

    def get_add_time(self):
        return f'{self.add_time}'

    def get_author(self):
        return self.author

    def get_likes(self):
        return self.like_users.all().count()

    def get_dislikes(self):
        return self.dislike_users.all().count()

    def get_tags(self):
        return self.tags.all()

    def get_num_answers(self):
        return self.answers.all().count()

    def get_answers(self):
        return self.answers.all()

    def rating(self) -> int:
        return self.like_users.all().count() - self.dislike_users.all().count()

    def __str__(self):
        return self.title

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

class Answer(models.Model):
    text = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    correct = models.BooleanField(default=False)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="answers")
    like_users = models.ManyToManyField(Member, related_name="answer_likes", blank=True)
    dislike_users = models.ManyToManyField(Member, related_name="answer_dislikes", blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", related_query_name="answer")

    def get_add_time(self):
        return f'{self.add_time}'

    def get_author(self):
        return self.author

    def get_likes(self):
        return self.like_users.all().count()

    def get_dislikes(self):
        return self.dislike_users.all().count()

    def rating(self) -> int:
        return self.like_users.all().count() - self.dislike_users.all().count()

    def __str__(self):
        return self.text

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

class TagManager(models.Manager):
    def popular_tags(self):
        return self.all().annotate(rating=Count('questions')).order_by('rating').reverse()[:5]


class Tag(models.Model):
    name = models.CharField(max_length=10)
    questions = models.ManyToManyField(Question, related_name="tags")
    rating = models.IntegerField(blank=True, null=True)

    objects = TagManager()

    def rating(self) -> int:
        return self.questions.all().count()
    
    def questions_by_tag(self):
        return self.questions.all()

    def __str__(self):
        return self.name

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

BEST_MEMBERS = [
    {'name': 'Mr. Korgi'},
    {'name': 'Mr. Zaits'},
    {'name': 'Mr. Kot'},
]
