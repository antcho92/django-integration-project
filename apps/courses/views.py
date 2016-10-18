from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all().order_by('name')
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    if request.method == 'POST':
        validation = Course.objects.add_course(request.POST)
        if validation[0]:
            return redirect(reverse('courses:index'))
        else:
            messages.error(request, validation[1])
    return redirect('/courses')

def destroy(request, id):
    #Course.objects.get(id=id).delete()
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)
def confirm_destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/courses')
