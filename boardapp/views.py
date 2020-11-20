from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from .forms import BoardForm

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required        
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request):
    user_name = request.GET['user_name']
    pk = request.GET['pk']
    post = BoardModel.objects.get(pk=pk)
    good_count = post.good

    if user_name in post.goodtext:
        post.good = post.good - 1
        post.goodtext = post.goodtext.replace(user_name+' ', '')
        post.save()
        data = {
            'good_mode': 'good-off',
            'good_count': post.good
        }
    else:
        post.good = post.good + 1
        post.goodtext = post.goodtext + user_name + ' '
        post.save()
        data = {
            'good_mode': 'good-on',
            'good_count': post.good,
        }
    return JsonResponse(data)
        
def readfunc(request):
    user_name = request.GET['user_name']
    pk = request.GET['pk']
    post = BoardModel.objects.get(pk=pk)

    if user_name in post.readtext:
        post.read = post.read - 1
        post.readtext = post.readtext.replace(user_name+' ', '')
        post.save()
        data = {
            'read_mode': 'read-off',
            'read_count': post.read
        }
    else:
        post.read = post.read + 1
        post.readtext = post.readtext + user_name + ' '
        post.save()
        data = {
            'read_mode': 'read-on',
            'read_count': post.read
        }
    return JsonResponse(data)


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    form_class = BoardForm
    # fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')