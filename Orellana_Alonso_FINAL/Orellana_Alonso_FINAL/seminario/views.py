from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Inscrito, Institucion
from .forms import InscritoForm
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class AuthorInfoView(APIView):
    def get(self, request, *args, **kwargs):
        author_info = {
            'nombre': 'Alonso Orellana',
            'edad': 22,
            'rut': '20881491-5',
        }
        return Response(author_info, status=status.HTTP_200_OK)

class HomePageView(TemplateView):
    template_name = 'home.html'

class InscritoListCreateView(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InstitucionListCreateView(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InstitucionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    success_url = reverse_lazy('home')









