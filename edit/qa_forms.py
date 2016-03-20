# -*- coding: utf-8 -*-
from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea, required=False)
    author = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    def save(self):
        self.cleaned_data['author'] = User.objects.get(id=1)
        ques = Question(**self.cleaned_data)

        ques.save()
        return ques


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())
    author = forms.IntegerField(initial=1,required=False)

    def __init__(self,*args,**kwargs):
        super(AnswerForm, self).__init__(*args,**kwargs)

    def save(self):
        self.cleaned_data['author'] = User.objects.get(id=1)
#        self.cleaned_data['question'] = Question.objects.get(id=int(self.cleaned_data['question']))
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer