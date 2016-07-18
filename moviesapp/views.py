from django.shortcuts import render
from .models import Movie
from django.utils import timezone


# Create your views here.
def movies_list(request):
    movies = Movie.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'moviesapp/movie.html', {'movies': movies})
