from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth


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
            return HttpResponseRedirect('/question/%s/' % question_id)
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
        return HttpResponseRedirect('/')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return HttpResponseRedirect('/')
        else:
            args['form'] = new_user_form
    return render(request, "register.html", args)

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = u'Error login or password'
            return render_to_response('login.html', args)
    else:
        return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')