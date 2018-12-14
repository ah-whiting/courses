from django.shortcuts import render, redirect
from .models import Course

def root(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create_course(request):
    if request.method == 'POST':
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc'],
        )
    return redirect('/')

def delete_course(request, id):
    if request.method == 'GET':
        context = {
            'course' : Course.objects.get(id = id)
        }
        return render(request, 'courses/delete_warning.html', context)
    if request.method == 'POST':
        Course.objects.get(id=id).delete()
    return redirect('/')

