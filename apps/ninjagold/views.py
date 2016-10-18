from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        print("New game started")
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninjagold/index.html')

def process_money(request):
    if request.method == 'POST':
        buildings = {
                'farm': random.randint(10, 20),
                'cave':random.randint(5, 10),
                'house': random.randint(2, 5),
                'casino': random.randint(-50, 50)
        }
        #checks if type of building is in the building object holding my gold
        if request.POST['building'] in buildings:
            #adds to the gold at the top
            result = buildings[request.POST['building']]
            request.session['gold'] += result
            not_casino = "Earned {} golds from the {}!".format(result, request.POST['building'])
            casino = "Entered a casino and {} {} golds.{}".format("won" if result > 0 else "lost", result if result > 0 else -result, " Yay!" if result > 0 else ".. Ouch..")
            result_dict = {
                'class': 'green' if result > 0 else "red",
                'activity': not_casino if request.POST['building'] != 'casino' else casino,
                'date': datetime.now().strftime('%Y/%m/%d %-I:%M %p')
            }
        request.session['activities'].append(result_dict)
        print(request.session['activities'])
        return redirect('/')
    else:
        return redirect('/')
def reset(request):
    if 'gold' in request.session:
        request.session['gold'] = 0
    if 'activities' in request.session:
        del request.session['activities']
    return redirect('/')
