from .models import FAQ
from django.db.models import Q
from .forms import QuestionForm
from django.shortcuts import render
from .ai_model.chat import response



def chat(request):
    questionForm = QuestionForm()

    if request.method == 'POST':
        questionForm = QuestionForm(request.POST)

        if questionForm.is_valid():
            question = questionForm.data['question']

            answer = response(question)

            return render(request, 'chat/answer.html', {'answer': answer})

        else:
            return render(request, 'chat/error_messages.html', {'error_messages': questionForm.errors})

    return render(request, 'chat/question_input.html', {'form': questionForm})


def FAQ_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    FAQs = FAQ.objects.filter(
        Q(question__icontains=q)
    )

    return render(request, 'chat/FAQ.html', {'FAQs': FAQs})
