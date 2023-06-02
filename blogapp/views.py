from django.shortcuts import render
from .forms import TemaForms
from .models import Tema


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def cad_tema(request):
    form = TemaForms
    if request.method == "POST":
        form = TemaForms(request.POST, request.FILES)
        if form.is_valid():
            ob = form.save()
            ob.save()
            form=TemaForms()
    return render(request, 'blog/cad_tema.html',{'form':form})


def temas(request):
    temas = Tema.objects.all()
    return render(request,'blog/temas.html',{'temas':temas})