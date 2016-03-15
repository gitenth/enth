from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer

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
    return render(request, 'index.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': posts.title,
        'id': posts.id,
        })

def popular_posts(request):
    posts = Question.objects.all().order_by('-rating')
    paginator, page = paginate(request, posts)
    return render(request, 'index.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': posts.title,
        'id': posts.id,
        })

def question(request, id):
    post = Question.objects.get(id=id)
    comment = Answer.objects.get(question__id=id)
    return render(request, 'quest.html', {
        'title': posts.title,
        'text': posts.text,
        'comment': comment.text,
        })
