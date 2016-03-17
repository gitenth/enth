from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

def post_list_all(request):
    posts = Question.objects.all().order_by('-id')
    paginator, page = paginate(request, posts)
    return render(request, 'main.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'post': posts,
        })

def popular_posts(request):
    posts = Question.objects.all().order_by('-rating')
    paginator, page = paginate(request, posts)
    return render(request, 'main.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'post': posts,
        })

def question(request, question_id):
    try:
        posts = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
       raise Http404
    comment = Answer.objects.filter(question__id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/question/%s' % post.id)
    else:
        form = AnswerForm()
    return render(request, 'quest.html', {
        'title': posts.title,
        'text': posts.text,
        'comment': comment,
        'form': form,
        'question_id': question_id
        })

def add_quest(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/question/%s/' % post.id)
    else:
        form = AskForm()
    return render(request, 'add_quest.html',{
        'form': form,
        })

def add_comment(request):
    if request.method == "POST":
        return render("OK")
    else:
        return HttpResponseRedirect('')