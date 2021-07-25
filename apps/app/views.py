from django.db import models
from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView


from .models import Quiz, Question, Answer


class QuizList(ListView):
    model = Quiz
    template_name = "app/quiz/quiz_list.html"


def QuizDetail(request, slug):
    template_name = 'app/quiz/quiz_detail.html'

    # get quiz context
    quiz = Quiz.objects.get(slug=slug)
    question_list = []

    for question in quiz.question_set.all():
        answer = question.answer_set.all()

        question_list.append([str(question), answer])

    context = {
        'quiz': quiz,
        'question_list': question_list,
    }

    return render(request, template_name, context)


def ResultDetail(request, slug):

    if request.method == "POST":
        template_name = 'app/quiz/result_detail.html'

        print(request.POST)
        
        quiz = Quiz.objects.get(slug=slug)
        question_list = quiz.get_questions()
        correct_list = []
        score = 0 

        for ques in question_list:
            ques_id = str(ques.id)
            if ques_id in request.POST:
                ans_id = request.POST[ques_id]
                ans = Answer.objects.get(pk=ans_id)

                if ans.correct:
                    correct_list.append("Correct")
                    score += 1
                else:
                    correct_list.append("Incorrect")
                    score -= 1
            else:
                correct_list.append("No answer")

        ques_cor_list = zip(question_list, correct_list)
        context = {
            'quiz': quiz,
            'ques_cor_list': ques_cor_list,
            'score': score,
        }

        return render(request, template_name, context)

