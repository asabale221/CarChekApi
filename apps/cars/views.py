from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from django.views import generic

from apps.cars.models import Car
from apps.cars.serializers import CarSerializers


class IndexView(generic.ListView):
    queryset = Car.objects.all()
    context_object_name = "cars"
    model = Car
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context


def search(request):
    if request.method == "GET":
        query = request.GET.get('search')
        if query:
            cars = Car.objects.filter(license_plate__contains = query)
            return render(request, 'result.html', {'cars':cars})
        else:
            return render(request, 'result.html', {})

# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all() #SELECT * FROM cars_car;
    serializer_class = CarSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['license_plate', ]
    
    

class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers