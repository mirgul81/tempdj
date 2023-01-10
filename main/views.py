from django.shortcuts import render, redirect, HttpResponse
from .models import Regions, Areas
from .forms import CreateRegionForm
from .forms import CreateAreaForm


def indexView(request):
    regions = Regions.objects.all()
    areas = Areas.objects.all()
    context = {
        'regions': regions,
        'areas': areas
    }
    return render(request, 'main/index.html', context)

def sverdlovView(request, pk):
    regions = Regions.objects.all()
    region = Regions.objects.get(id=pk)
    areas = Areas.objects.all()

    context = {
        'name': region.name,
        'regions': regions,
        'areas': areas,
        'region': region,

    }
    return render(request, 'main/sverdlov.html', context)



def batkenView(request, pk):
    areas = Areas.objects.all()
    area = Areas.objects.get(id=pk)
    regions = Regions.objects.all()
    context = {

        'regions': regions,
        'areas': areas,
        'area': area,
    }

    return render(request, 'main/batken.html', context)

def create_regionView(request):
    if request.method == 'POST':
        form = CreateRegionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        else:
            return HttpResponse("ERROR")

    form = CreateRegionForm()
    context = {
        'form': form
    }
    return render(request, 'main/create/create.html', context)



def create_areaView(request):

    if request.method == 'POST':
        form = CreateAreaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        else:
            return HttpResponse("ERROR")

    form = CreateAreaForm()
    context = {
        'form': form
    }
    return render(request, 'main/create/create.html', context)

def update_regionView(request, id):
    region = Regions.objects.get(id=id)
    if request.method == 'POST':
        form = CreateRegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        return HttpResponse("invalid data")

    form = CreateRegionForm(instance=region)
    context = {'form':form}
    return render(request, 'main/create/create.html', context)

def delete_regionView(request, id):
    region = Regions.objects.get(id=id)
    region.delete()
    return redirect(to='main:index')


def update_areaView(request, id):
    area = Areas.objects.get(id=id)
    if request.method == 'POST':
        form = CreateAreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        return HttpResponse("invalid data")

    form = CreateAreaForm(instance=area)
    context = {'form':form}
    return render(request, 'main/create/create.html', context)


def delete_areaView(request, id):
    area= Areas.objects.get(id=id)
    area.delete()
    return redirect(to='main:index')
