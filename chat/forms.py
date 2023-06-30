from django.forms import ModelForm
from .models import QuestionModel


class QuestionForm(ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'