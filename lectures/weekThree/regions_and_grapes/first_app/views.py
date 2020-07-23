from django.shortcuts import render, redirect
from .models import Region, Grape, Producer
from django.contrib import messages

# Create your views here.
def index(request):
    # print(request.method)
    # print(request.POST)
    # print(request.GET)
    # print(type(request.session))
    all_regions = Region.objects.all()
    print('total amount of regions', all_regions.count())
    all_grapes = Grape.objects.all()
    print('total amount of grapes', all_grapes.count())
    all_producers = Producer.objects.all()
    print('total amount of producers', all_producers.count())

    context = {
        'regions': all_regions,
        'grapes': all_grapes,
        'producers': all_producers
    }
    request.session['count'] = 1
    return render(request, 'index.html', context)

def show_name(request, name):
    print('-'*50)
    print(f'name is: {name}')
    print('-'*50)
    return redirect('/')

def process_form(request):
    print(request.method)
    print(request.POST)
    print(request.POST['name'])
    print(request.POST['location'])
    print(request.session['count'])
    print(request.GET)

    request.session['name_from_form'] = request.POST['name']
    request.session['location_from_form'] = request.POST['location']

    # context = {
    #     'name_to_template': request.POST['name'],
    #     'location_to_template': request.POST['location']
    # }

    return redirect('/success')

def success(request):

    print(request.POST)
    print(request.GET)
    if 'name_from_form' in request.session:
        context = {
            'name_to_template': request.session['name_from_form'],
            'location_to_template': request.session['location_from_form']
        }

    return render(request, 'process.html', context)

def add_region(request):
    print('request.POST', request.POST)
    message_from_model = Region.objects.validate_region(request.POST)
    print('model message in views', message_from_model)

    if message_from_model['status'] == True:
        region_created = Region.objects.create(name=request.POST['form_name'], latitude=request.POST['form_latitude'], longitude=request.POST['form_longitude'])
        print(region_created)
    else:
        print(message_from_model['messages'])
        for mess in message_from_model['messages']:
            messages.error(request, mess)

    return redirect('/')

def add_grape(request):
    print(request.POST)
    region_to_add = Region.objects.get(id=request.POST['form_region'])
    print(region_to_add)
    Grape.objects.create(name=request.POST['form_name'], description=request.POST['form_description'], region=region_to_add)
    return redirect('/')

def add_producer(request):
    print(request.POST)
    Producer.objects.create(name=request.POST['form_name'])
    return redirect('/')

def region_to_producer(request):
    # get the region
    region = Region.objects.get(id=request.POST['form_region'])
    # get the producer
    producer = Producer.objects.get(id=request.POST['form_producer'])

    # add the connection
    # region.produced_by.add(producer)

    producer.regions.add(region)
    
    return redirect('/')

