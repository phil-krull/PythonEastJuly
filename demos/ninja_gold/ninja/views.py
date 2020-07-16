from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

import random

# Create your views here.
def index(request):
    print('total gold in index')
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    print('='*50)
    print(request.session['total_gold'])
    print(request.session['activities'])
    return render(request, 'index.html')

def process(request):
    print('in process method')
    if request.method == 'POST':
        print(request.POST)
        if request.POST['building'] == 'farm':
            gold_amount = randint(10, 20)
        elif request.POST['building'] == 'cave':
            gold_amount = randint(5, 10)
        elif request.POST['building'] == 'house':
            gold_amount = randint(2, 5)
        elif request.POST['building'] == 'casino':
            gold_amount = random.randint(-50, 50)

        print('*'*20, ' random number ','*'*20)
        print(gold_amount)

        request.session['total_gold'] += gold_amount
        print('total_gold', request.session['total_gold'])

        # build message for template
            # know the gold earn/lost
            # what building
            # time
            # way store the past experiences
        current_time = datetime.now()
        updated_time = datetime.strftime(current_time, '%Y/%m/%d %I:%m %p')

        if gold_amount < 0:
            # lost money
            request.session['activities'].append({'message': f"Enter a casino and lost {abs(gold_amount)} golds OUCH...... {updated_time}", 'color': 'red' })
        else:
            request.session['activities'].append({'message': f"Earned {gold_amount} from the {request.POST['building']}! {updated_time}", 'color': 'green' })

    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')