from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyform/index.html')

def process(request):
    if request.method == 'POST':
        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        return redirect('/survey/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'surveyform/results.html')

def goback(request):
    return redirect('/')
