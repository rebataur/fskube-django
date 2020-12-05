from django.shortcuts import render, HttpResponse
from .models import Person
# Create your views here.
def index(request):
    # Create an object
    p = Person.objects.create(name='Aran Karter')
    persons = Person.objects.filter(name='Aran Karter')

    # calculate monthly sales
    visits = 1000
    sales = 600
    conversion_rates = sales/visits*100
    context = {
        'conversion' : conversion_rates
    }

    return render(request,'app/index.html',context=context)
