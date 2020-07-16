from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(type(request.session))
    request.session['count'] = 1
    return render(request, 'index.html')

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