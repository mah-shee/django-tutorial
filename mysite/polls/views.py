from django.http import Http404 
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.htmls', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Qestion.object.order_by('_pub_date')[:5]
    context = {'latest_quesion_list': latest_question_list,}
    return render(request, 'polls/index.html', context)

def vote(request, question_id):

