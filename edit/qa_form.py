# -*- coding: utf-8 -*-
from django.forms import ModelForm
from qa.models import Question, Answer

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']