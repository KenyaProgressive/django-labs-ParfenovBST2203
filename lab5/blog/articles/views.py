
from django.shortcuts import render
from articles.models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

@login_required
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form["errors"] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form["errors"] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
    

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        data_is_exist = username and email and password and confirm_password

        if not data_is_exist:
            return render(request, 'sign_up.html', {
                'error': 'Не все поля заполнены',
                'username': username,
                'email': email
            })
        
        try:
            User.objects.get(username=username)
            return render(request, 'sign_up.html', {
                'error': 'Пользователь с таким именем уже существует',
                'username': '',
                'email': email
            })
        
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('archive')
        
    return render(request, 'sign_up.html')

def sign_in(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Заполнены ли поля
        if not (username and password):
            return render(request, 'sign_in.html', {
                'error': 'Заполните все поля!',
                'username': username
            })
        
        # Аутентификация пользователя

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'sign_in.html', {
                'error': 'Неверное имя пользователя или пароль',
                'username': username
            })
        
    return render(request, 'sign_in.html')


def account_logout(request):
    logout(request)
    return redirect('archive')
