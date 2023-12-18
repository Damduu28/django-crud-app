from django.shortcuts import render, redirect
from .models import Crud
# Create your views here.

from .forms import CrudForm

def home(request):
    return render(request, "crud/home.html")

def crudPage(request):
    result = request.GET.get('result') if request.GET.get('result') is not None else 5
    result = int(result)
    if request.user.is_authenticated:
        cruds = Crud.objects.filter(user=request.user)[:result]
    else:
        cruds = []
        message = 'You have no'
    context = {"cruds": cruds}
    return render(request, "crud/crud.html", context)

def createCrud(request):
    if request.method == "POST":
        form = CrudForm(request.POST, request.FILES)
        if form.is_valid():
            crud = form.save(commit=False)
            crud.user = request.user
            crud.color = request.POST.get('color')
            crud.save()
            return redirect('crud')   
    else:
        form = CrudForm()
    context = {'btn': 'Create', 'form': form}
    return render(request, "crud/create_form.html", context)

def updateCrud(request, pk):
    crud = Crud.objects.get(id=pk)
    if request.method == "POST":
        form = CrudForm(request.POST, request.FILES, instance=crud)
        if form.is_valid():
            crud = form.save(commit=False)
            crud.color = request.POST.get('color')
            crud.save()
            return redirect('crud')
    else:
        form = CrudForm(instance=crud)
    context = {'btn': 'Update', 'form': form, 'crud': crud}
    return render(request, "crud/create_form.html", context)

def deleteCrud(request, pk):
    crud = Crud.objects.get(id=pk)
    crud.delete()
    return redirect('crud')