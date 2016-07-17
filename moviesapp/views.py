from django.shortcuts import render


# Create your views here.
def movies_list(request):
    return render(request, 'moviesapp/movie.html', {})
