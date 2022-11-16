from django.db import models
from django.contrib.auth.models import User
import django.contrib.auth.backends
import os.path


class Member(models.Model):
    info = models.OneToOneField(django.contrib.auth.backends.UserModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default="static/img/korgi.jpg", upload_to="app/static/img", blank=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.info.__str__()

    def get_avatar(self):
        return "img/" + os.path.basename(self.avatar.name)

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

class Question(models.Model):
    title = models.CharField(max_length=77, unique=True)
    text = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="questions")
    like_users = models.ManyToManyField(Member, related_name="question_likes", blank=True)
    dislike_users = models.ManyToManyField(Member, related_name="question_dislikes", blank=True)

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

    def __str__(self):
        return self.text

    def get_add_time(self):
        return f'{self.add_time}'

    def get_author(self):
        return self.author

    def get_likes(self):
        return self.like_users.all().count()

    def get_dislikes(self):
        return self.dislike_users.all().count()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

class Tag(models.Model):
    name = models.CharField(max_length=10)
    questions = models.ManyToManyField(Question, related_name="tags")
    rating = models.IntegerField(blank=True, null=True)
    
    def questions_by_tag(self):
        return self.questions.all()


    def __str__(self):
        return self.name

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-------------------

ANSWERS = [
    {
        'id': answer_id,
        'text': f'Text of answer #{answer_id}',
        'rating': f'{answer_id}'

    } for answer_id in range(10)
]

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answers_number': question_id * question_id,
        'rating': f'{question_id}',
        'answers': ANSWERS,
        'tags': ['kotiki', 'sobachki', 'zayki']

    } for question_id in range(10)
]

IS_AUTHORISATED = False

POPULAR_TAGS = [
    {'name': 'kotiki', 'style': 'custom-tags-max-popular'},
    {'name': 'sobachki', 'style': 'custom-tags-popular'},
    {'name': 'zayki', 'style': 'custom-tags-min-popular'},
]

BEST_MEMBERS = [
    {'name': 'Mr. Korgi'},
    {'name': 'Mr. Zaits'},
    {'name': 'Mr. Kot'},
]

HOT_QUESTIONS = [
    1, 3, 7
]
