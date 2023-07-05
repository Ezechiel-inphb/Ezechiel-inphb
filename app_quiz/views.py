from django.shortcuts import render
from .models import Game
from django.http import JsonResponse
from quest_app.models import Question, Answer
from app_résultat.models import Result

def jeu_biblique(request):
    quiz = Game.objects.get(pk=1)
    return render(request,'jeu.html',{'obj':quiz})


def quest_data(request,):
    quiz = Game.objects.get(pk=1)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz(request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)
        
        user = request.user
        quiz = Game.objects.get(pk=1)

        score = 0
        multiplier = 100/quiz.number_of_quest
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:  
                            correct_answer = a.text

                results.append({str(q): {'correct_answer':correct_answer, 'answered':a_selected}})
            else:
                results.append({str(q):'not answered'})
            
        score_ = score*multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.score_to_pass:
            return JsonResponse({'passed':True, 'score':score_ , 'results':results})
        else:
            return JsonResponse({'passed': False, 'score':score_ , 'results':results})