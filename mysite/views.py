from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from slide.models import Slide

# Create your views here.
def index(request):
    #获取slide表的数据
    slides = Slide.objects.all()
    return render(request, 'index.html', {'slides':slides})