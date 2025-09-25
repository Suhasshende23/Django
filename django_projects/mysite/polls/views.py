from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.template import loader
from .models import *
from django.views.generic import *
def index(request):
    # top_five_questions=Questions.objects.all()
    top_two_questions=Questions.objects.order_by('-pub_date')[:5]  #THis will order the query result
    template=loader.get_template('polls/index.html')
    context={'latest_poll':top_two_questions}
    return HttpResponse(template.render(context,request))  

def detail(request, question_id):
    # try:
    #    question=Questions.objects.get(pk=question_id)
    # except Questions.DoesNotExist:
    #     raise Http404("404 Page not found")
    question=get_object_or_404(Questions,pk=question_id)
    context={"question":question}
    return render(request,'polls/detail.html',context)


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/vote.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))