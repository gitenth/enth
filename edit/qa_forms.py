# -*- coding: utf-8 -*-
from django.forms import ModelForm
from qa.models import Question, Answer

class AskForm(ModelForm):
    def save(self, author, commit=True):
        # Don't commit the results yet
        news = AskForm.save(self, commit=False)
        news.author = author
        if commit:
            news.save()
        return news
    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']