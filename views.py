from django.shortcuts import render, redirect
from .forms import CaseFileForm
from .models import CaseFile


def index(request):
    last_cases = CaseFile.objects.order_by('-edited_on')
    return render(request, 'book/index.html', {'last_cases': last_cases})


def create(request):
    if request.method == 'POST':
        file = CaseFile()
        file.save()
        return redirect(f'/edit/{file.pk}')


def edit(request, pk):
    file = CaseFile.objects.get(pk=pk)
    if request.method == 'POST':
        form = CaseFileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/')
    elif request.method == 'GET':
        form = CaseFileForm(initial=file.__dict__)
        context = {
            'file': file,
            'form': form
        }
        return render(request, 'book/edit.html', context)


def delete(request, pk):
    if request.method == 'POST':
        CaseFile.objects.get(pk=pk).delete()
        return redirect('/')
    elif request.method == 'GET':
        return render(request, 'book/delete.html', {'pk': pk})
