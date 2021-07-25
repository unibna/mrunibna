from random import randint
from django.db import models
from django.db.models.fields import IPAddressField
from django.utils.text import slugify
from django.utils import timezone

from apps.post.models import Category
from apps.user.models import CustomUser


DIFFCULT_LEVEL = [
    (1, "Easy"),
    (2, "Medium"),
    (3, "Hard"),
]

class Quiz(models.Model):
    title = models.CharField(max_length=128)
    slug  = models.SlugField(max_length=64, unique=True, null=True, blank=True)
    topic = models.ManyToManyField(Category)
    number_of_question = models.IntegerField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    time  = models.IntegerField(default=15)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # generate slug automatically
        ran_number = randint(1,999999)
        self.slug = slugify(self.title, ran_number)
        # update the number of questions automatically
        return super().save(*args, **kwargs)

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    text = models.CharField(max_length=1024)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    level = models.IntegerField(choices=DIFFCULT_LEVEL)

    def __str__(self):
        return f"{self.quiz.title} - {self.text}"

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=1024)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct  = models.BooleanField()

    def __str__(self):
        return self.text