from django.shortcuts import render, redirect, get_object_or_404
from .models import Car

# View to list all cars
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

# View to add a new car
def add_car(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        description = request.POST['description']
        Car.objects.create(make=make, model=model, year=year, price=price, description=description)
        return redirect('car_list')
    return render(request, 'cars/add_car.html')

# View to delete a car
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('car_list')
