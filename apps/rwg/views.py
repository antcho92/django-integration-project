from django.shortcuts import render, redirect
import random, string

# taken from http://stackoverflow.com/questions/2030053/random-strings-in-python
def randomword(length):
    return ''.join(random.choice(string.digits+string.uppercase)for i in range(length))

# Create your views here.
def index(request):
    if not 'attempts' in request.session:
        request.session['attempts'] = 1
    else:
        request.session['attempts'] += 1
    request.session['word'] = randomword(14)
    return render(request, 'rwg/index.html')


def generate(request):
    return redirect('/')

def reset(request):
    if request.method == 'GET':
        try:
            del request.session['attempts']
        except:
            pass
        return redirect('/generate')
