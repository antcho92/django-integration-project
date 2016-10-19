from django.shortcuts import render, redirect
from .models import Course
from ..loginreg.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count

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

def users_courses(request):
    courses = Course.objects.annotate(number_of_users=Count('users'))
    print(len(courses))
    print(courses[4].number_of_users)
    print(courses[1].name)

    context = {
        'courses': courses,
        'users': User.objects.all().order_by('id')
    }
    return render(request, 'courses/users_courses.html', context)

def add_user(request):
    if request.method == 'POST':
        course = Course.objects.get(id=request.POST['course'])
        print(course)
        user = User.objects.get(id=request.POST['user'])
        print(user)
        course.users.add(user)
    return redirect(reverse('courses:users_courses'))
