from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    latest_movies = Movie.objects.order_by('-update_time')[:10]
    context = {'latest_movies': latest_movies}
    return render(request, 'movie_app/index.html', context)

def search(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    if not query:
        return render(request, 'movie_app/search_results.html', {'error': '请输入搜索关键词'})
    
    movie_list = Movie.objects.filter(title__icontains=query)
    
    if category_filter and category_filter != 'all':
        movie_list = movie_list.filter(category=category_filter)
    
    paginator = Paginator(movie_list, 10)  # 每页显示10条
    page = request.GET.get('page')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，显示第一页
        movies = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，显示最后一页
        movies = paginator.page(paginator.num_pages)
    
    categories = Movie.objects.values_list('category', flat=True).distinct()
    context = {
        'movies': movies,
        'query': query,
        'categories': categories,
        'selected_category': category_filter
    }
    return render(request, 'movie_app/search_results.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_app/detail.html', {'movie': movie})

def category(request, category):
    movie_list = Movie.objects.filter(category=category).order_by('-update_time')
    paginator = Paginator(movie_list, 10)
    page = request.GET.get('page')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    all_categories = Movie.objects.values_list('category', flat=True).distinct()
    context = {
        'movies': movies,
        'category': category,
        'categories': all_categories
    }
    return render(request, 'movie_app/category.html', context)