from demo.models import Genre
#from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView

class GenreListView(ListView):
        model = Genre
        context_object_name = 'Approved_genres'
        template_name = 'home.html'