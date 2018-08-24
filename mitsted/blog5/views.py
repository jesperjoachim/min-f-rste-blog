from django.shortcuts import render
from .models import  Opslag
from django.utils import timezone

# Create your views here.
def post_list(request):
    opslag = Opslag.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog5/post_list.html', {'opslag': opslag})
