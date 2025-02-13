from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.


def index(request):
    movie = Movie.objects.order_by("pk")
    context = {
        "movie": movie,
    }
    return render(request, "movieapp/index.html", context)


def create(request):
    if request.method == "POST":
        # title = request.POST.get('title')0000000000000000000000000000000000
        # content = request.POST.get('post')
        # Article.objects.create(
        #     title=request.POST.get('title'),
        #     content=request.POST.get('content')
        # )

        # DB에 저장하는 로직
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movieapp:index")
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movieapp/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    movie = Movie.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        "movie": movie,
    }
    return render(request, "movieapp/detail.html", context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            movie_form.save()
            return redirect("movieapp:detail", movie.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        movie_form = MovieForm(instance=movie)
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movieapp/update.html", context)


def delete(request, pk):

    movie = Movie.objects.get(id=pk)
    movie.delete()

    return redirect("movieapp:index")
