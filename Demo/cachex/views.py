from django.shortcuts import render
from django.views.decorators.cache import cache_page
 
@cache_page(60 * 1) # Cache the view for 1 minutes
def index(request):
    return render(request, 'cachex/index.html')