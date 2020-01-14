from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'quest'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[::-1]

class DetailView(generic.DetailView):
    model = Question
    context_object_name = 'quest'

    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    context_object_name = 'quest'

    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'quest': question,
            'error_message': "You didn't select a choice.",
        }
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=[question.id]))
        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))


# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.urls import reverse

# from .models import Question, Choice
# # Create your views here.

# def index(request):
#     questions = Question.objects.all()
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     return render(request, "polls/index.html", {'quest': questions} )

# ##import get_object_or_404 from django.shortcuts
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'quest': question})

# 

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'quest': question})






# '''
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")

#     return render(request, 'polls/detail.html', {'quest': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def questi(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     context = {
#         'question': question

#     }
#     return render(request, 'polls/questi.html', context)

# #import Http404
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'q': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
# '''